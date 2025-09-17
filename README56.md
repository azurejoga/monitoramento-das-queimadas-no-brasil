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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4741f45a-5e11-3486-8c2f-1d3f653ef23e | -14.7625 | -51.7086 | 2025-09-17 07:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| e3a73270-96b4-3b99-9594-219d7dbb684a | -14.8013 | -51.7033 | 2025-09-17 07:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 17843349-c863-3f08-92d6-eb08b47b2c5e | -14.7819 | -51.706 | 2025-09-17 07:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 113.4 |
| a50ffd39-6fae-33d3-9d4e-926d240b4df2 | -14.8009 | -51.7248 | 2025-09-17 07:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 4924f9b1-dfb6-342f-a97b-a2861bbdaba5 | -14.7629 | -51.6872 | 2025-09-17 07:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| baa2c9be-6c90-3e89-b2b6-12f940433fbe | -10.6731 | -46.5154 | 2025-09-17 07:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 1e72bd69-efdd-34dd-8d20-0b037f8c3021 | -14.8987 | -51.6684 | 2025-09-17 07:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 723d2f45-52fb-3e57-98ff-375362c7e1d8 | -10.6925 | -46.4904 | 2025-09-17 07:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 6c8abca9-1f1d-391d-8860-17c3d073a914 | -10.6727 | -46.5379 | 2025-09-17 07:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| e34c3820-c248-33de-a5e7-2087881e73d2 | -14.8983 | -51.6899 | 2025-09-17 07:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| ac0f4225-34f1-3666-b59e-9e7c53bc48bf | -10.6925 | -46.4904 | 2025-09-17 07:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 58436c9f-ce06-3bb4-bd37-892eca54d04e | -10.6731 | -46.5154 | 2025-09-17 07:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 9d95a140-a5ff-3dfd-a9f9-32281de55a37 | -10.6727 | -46.5379 | 2025-09-17 07:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 8b4b06bd-1c9a-3476-a0ab-4386d5ebdb99 | -10.6738 | -46.4703 | 2025-09-17 07:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 6cbe1777-fc43-33aa-a3ca-96964acc053b | -10.6925 | -46.4904 | 2025-09-17 07:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 97f4fa0d-9d1f-3f29-9ad8-dc6c2e3ea9b7 | -10.6734 | -46.4928 | 2025-09-17 07:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 33555964-4d24-39ac-b55e-ee141c3e7c71 | -10.6925 | -46.4904 | 2025-09-17 07:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 9e8dc9c6-1b99-30c4-a90c-7c6cba81b18a | -10.6734 | -46.4928 | 2025-09-17 07:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| c8449a67-02f8-3644-8ea7-d792a2fc3b68 | -10.6734 | -46.4928 | 2025-09-17 08:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 43127a8b-cb5f-3664-a628-125d1a895b92 | -10.6925 | -46.4904 | 2025-09-17 08:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 4952a4f2-22e2-3228-bdfb-51eeb00c0221 | -12.729 | -48.0068 | 2025-09-17 08:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 1e417a3d-aebd-39d6-ad88-128bc547cfe1 | -10.6925 | -46.4904 | 2025-09-17 08:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 8a946339-4c81-3aac-967b-f4e4cb7cdd33 | -14.5734 | -47.4114 | 2025-09-17 08:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 220e3f57-90bd-301c-8948-72567d2b27ab | -12.7286 | -48.029 | 2025-09-17 08:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 412ddd4b-d2b1-383b-b84a-87511965d6cf | -14.5739 | -47.3887 | 2025-09-17 08:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 0d89fea5-5c8d-3f72-83d5-cb2a9970500d | -12.7294 | -47.9845 | 2025-09-17 08:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 56c1a10b-44f5-3a22-b940-5ad602d48446 | -12.729 | -48.0068 | 2025-09-17 08:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 2dd890e3-5d86-35e5-b24d-1ac5a8d3571e | -14.7819 | -51.706 | 2025-09-17 08:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 4c35cff5-902b-379e-a21f-4440586b2200 | -14.7815 | -51.7274 | 2025-09-17 08:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| c63eb06f-010d-3e51-82ec-525d1e893a84 | -14.8013 | -51.7033 | 2025-09-17 08:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| cdcb8635-e6cd-393d-8f01-627aa694a0ab | -14.8009 | -51.7248 | 2025-09-17 08:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 3535093d-aafd-3053-a31b-3c5cf61aaebf | -12.3865 | -51.4135 | 2025-09-17 08:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| d3d9cd44-2c14-3011-a55b-e5f0a3b06ae3 | -7.5996 | -44.5872 | 2025-09-17 09:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 02ab3dd3-ffef-336e-a01d-280bb1fe806e | -7.5996 | -44.5872 | 2025-09-17 10:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| e1bdd8a1-eb1d-34e5-8544-56c1e71c7257 | -10.6925 | -46.4904 | 2025-09-17 10:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 798c2dbe-9d86-3833-8ff0-eb33f555e491 | -10.6731 | -46.5154 | 2025-09-17 10:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 276.6 |
| 0126f42f-d144-3ebc-8c5e-ed564a4908bb | -10.6734 | -46.4928 | 2025-09-17 10:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 209.3 |
| 3ee8ce42-4e67-3873-bc5e-47dd0728db68 | -10.6921 | -46.513 | 2025-09-17 10:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 7a3ce2ba-71bd-363a-82ac-07b3d5351f1c | -10.6727 | -46.5379 | 2025-09-17 10:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 6447353c-1a58-30e9-950f-bccc1d44eb46 | -10.6734 | -46.4928 | 2025-09-17 10:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 4076c81e-4194-33f0-96c4-585f5fcce3b6 | -10.6731 | -46.5154 | 2025-09-17 10:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 5167b621-9bb8-3bec-9dd1-807c09c786a7 | -10.6921 | -46.513 | 2025-09-17 11:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 3db5c618-b5de-34b2-8e7c-8e991cb8725f | -10.6731 | -46.5154 | 2025-09-17 11:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 4793c6a7-0f3f-3d58-a681-397f5758fb99 | -9.1236 | -44.8849 | 2025-09-17 11:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 32bc7f67-61bf-311d-9d70-561bef38643d | -9.1239 | -44.862 | 2025-09-17 11:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 97822898-8c75-3936-876a-d1d8f34b055a | -12.7115 | -45.7993 | 2025-09-17 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| e1fdfe29-02ea-320b-86d2-3f99288f8bab | -10.6731 | -46.5154 | 2025-09-17 11:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| d12b0234-ad6e-37df-a54e-0e0d1b807685 | -9.1236 | -44.8849 | 2025-09-17 11:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 97174782-7042-3dab-a130-6c3be46f42b0 | -10.6734 | -46.4928 | 2025-09-17 11:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 52357908-6122-32fe-be0e-447d49ca1b59 | -8.8958 | -47.8683 | 2025-09-17 11:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 4bf26d02-eb5b-3c11-841b-74a766219a35 | -10.6925 | -46.4904 | 2025-09-17 11:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 328c86b4-8460-3c4c-b552-7ef656b5a569 | -10.6925 | -46.4904 | 2025-09-17 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 189.2 |
| e3ec91c7-1a42-3ece-9c6c-4d086150bfa2 | -12.7106 | -47.9649 | 2025-09-17 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| dd303b42-1c45-3948-aba5-4ca7f837a20e | -10.6734 | -46.4928 | 2025-09-17 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 153.6 |
| f2566ac6-28fc-37cd-bbb0-e4ff3c8e7240 | -10.6731 | -46.5154 | 2025-09-17 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 255.4 |
| 761d8e20-0a9b-3396-b1f1-08d26a0e73d1 | -11.1919 | -47.3896 | 2025-09-17 11:20:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 08ce7e64-7770-3f94-b38d-8eacd25374b5 | -9.1236 | -44.8849 | 2025-09-17 11:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| e272d22f-86d4-3ac2-940c-146e8e02143a | -9.1239 | -44.862 | 2025-09-17 11:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| fb9f0b15-b062-363b-8f7c-a041f21eab97 | -8.557 | -46.3509 | 2025-09-17 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 772418e3-4b17-3047-89f3-c6ef13b05f6f | -10.6921 | -46.513 | 2025-09-17 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 237.5 |
| 07bb1208-db62-3942-b2a9-84664b0a13cd | -10.6731 | -46.5154 | 2025-09-17 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 133.5 |
| ae42b054-23d6-3412-9cbf-07eb21ee7f4d | -9.1239 | -44.862 | 2025-09-17 11:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| cb8c4997-8116-3a2f-982b-1d74a50c8193 | -8.4787 | -45.0932 | 2025-09-17 11:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.8 |
| bd75f08a-eb01-3f9a-84af-f35429e90971 | -9.1236 | -44.8849 | 2025-09-17 11:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 21d7ddd3-d65c-3271-9058-f0fe1df93539 | -10.6921 | -46.513 | 2025-09-17 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 55c79098-3582-3bd2-b1a3-28bbbcaab3f3 | -11.1919 | -47.3896 | 2025-09-17 11:30:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| f46de2b5-8ace-3681-b0ba-9dda990b50d0 | -12.7482 | -48.0041 | 2025-09-17 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| c766f1e8-5f02-3c98-8e68-66c86f28323f | -10.6467 | -42.3141 | 2025-09-17 11:40:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 120.0 |
| ab3483b1-9156-39e5-8f65-93010b7655a0 | -12.7286 | -48.029 | 2025-09-17 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 1e42315e-156e-37db-93d1-73c9206391eb | -10.6921 | -46.513 | 2025-09-17 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 3d6f911f-f490-3a57-9f9d-c43e6546b8f6 | -10.6731 | -46.5154 | 2025-09-17 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| c01cc188-a35d-3b54-92f7-006c095e85b8 | -12.729 | -48.0068 | 2025-09-17 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 07587610-bccb-3a65-b351-b9cf86f44479 | -11.5775 | -48.2926 | 2025-09-17 11:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| a6852d81-27ac-36c9-95fd-3d914402a4bc | -9.1239 | -44.862 | 2025-09-17 11:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 1967dee5-bb64-3392-847e-1ebdeda96f04 | -9.1236 | -44.8849 | 2025-09-17 11:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 160.1 |
| a8ef0700-cec8-3a59-ad9b-c9968852b739 | -12.7478 | -48.0263 | 2025-09-17 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 932f6acc-23d7-3ab0-b962-0a88bab853e8 | -12.7106 | -47.9649 | 2025-09-17 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| a29980a7-961a-39c9-b41c-d3dc3a67c413 | -8.6313 | -46.4329 | 2025-09-17 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 4c87d5b0-fac5-3c5b-8c93-28a8063821ff | -12.0047 | -46.6989 | 2025-09-17 11:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| cd8235ba-426c-3545-9be3-b98b17304b15 | -12.7478 | -48.0263 | 2025-09-17 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| ea77d2a3-de9f-3f8d-a510-e78591de7a30 | -12.7106 | -47.9649 | 2025-09-17 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 126.2 |
| fc45e8bd-9046-3210-bbc8-5e2a994831ef | -12.729 | -48.0068 | 2025-09-17 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 30e10c6a-466d-3748-a466-0381b0230b62 | -8.6887 | -46.3599 | 2025-09-17 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 6ccf8bf3-e374-3e2c-a2af-d04a83b542ad | -8.631 | -46.4553 | 2025-09-17 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| d6fcdf60-6fb5-3c17-9b2a-d9ae8ccd0c8d | -11.1919 | -47.3896 | 2025-09-17 11:50:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 5dd94301-188c-348f-8fde-42e12d775849 | -10.6921 | -46.513 | 2025-09-17 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| e4e28d60-f635-39dc-ad6f-2049180e39c8 | -8.6699 | -46.3618 | 2025-09-17 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| a917c10a-eadb-3b99-b890-2be5f51e3bf4 | -9.1239 | -44.862 | 2025-09-17 11:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 106.5 |
| f7307bec-4f34-352f-b8f7-36e066421967 | -8.1572 | -46.747 | 2025-09-17 11:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 659dc208-4026-3fed-bd61-8446a1198431 | -12.7482 | -48.0041 | 2025-09-17 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| e3a3893b-abc6-337c-9222-eaec5a0438c0 | -8.9917 | -46.2609 | 2025-09-17 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 189.8 |
| f89f5a53-8d40-30d9-9024-9a6059d9f729 | -9.1236 | -44.8849 | 2025-09-17 11:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 143.2 |
| e85ac192-65c4-37b5-bdce-79daf8315546 | -8.9917 | -46.2609 | 2025-09-17 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 70a8222d-bbee-350f-8423-302fb9348f30 | -8.9728 | -46.263 | 2025-09-17 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| f762c902-a750-3185-9440-fb86ce2ce99c | -12.7482 | -48.0041 | 2025-09-17 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 0021fc81-d7c8-3698-a79e-fe102c381fe2 | -12.7294 | -47.9845 | 2025-09-17 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| ea2e7962-b8fa-3c52-88af-c3a22b29040a | -7.581 | -44.566 | 2025-09-17 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| b8eaa446-0a3f-36f3-9ec7-01a464886f1a | -8.6699 | -46.3618 | 2025-09-17 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| bae105aa-4fd5-37f1-8c2a-442bc8f88fb8 | -12.729 | -48.0068 | 2025-09-17 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 08834ecb-1d2f-3213-9173-9e09274c7e8e | -8.6887 | -46.3599 | 2025-09-17 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 146.9 |


[Clique aqui para ver as próximas entradas](README57.md)
