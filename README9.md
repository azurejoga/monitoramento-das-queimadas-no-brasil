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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23991024-415e-39bb-9b5e-c51557e8f579 | -5.7567 | -45.1067 | 2026-09-12 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 42039948-99a2-3d36-880e-0609168b2c8a | -10.2206 | -50.373 | 2026-09-12 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 362889b9-e662-370f-94bb-df55fb74818c | -5.7569 | -45.084 | 2026-09-12 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 179.2 |
| 1a4de40f-b6d2-3a6a-a3c3-0dafc405e98e | -6.2429 | -51.6939 | 2026-09-12 02:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 6ad293be-943e-3611-9610-da784a21b88d | -10.7018 | -54.1458 | 2026-09-12 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| c0cf3188-1155-311b-af5b-4e650e08a98f | -12.1501 | -64.1414 | 2026-09-12 02:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 71.0 |
| bd3b40f4-d3d7-317c-8593-c59a19b43505 | -3.2314 | -46.9376 | 2026-09-12 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 114c2f90-f1c9-39da-884d-d23daab74ad0 | -18.6668 | -41.9962 | 2026-09-12 02:10:00 | GOES-19 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 115.0 |
| 12e9e63b-9322-333c-ac80-45f795f18e07 | -2.7331 | -57.6271 | 2026-09-12 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 76f216d0-9c85-3090-ae85-1a466d4d2716 | -4.3587 | -47.7853 | 2026-09-12 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| fdeb5603-08d6-3c19-9952-4413b28a911a | -5.7754 | -45.1053 | 2026-09-12 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 197.2 |
| de7c541b-8a28-3441-a6d2-a34991580a96 | -3.2313 | -46.9596 | 2026-09-12 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 160.3 |
| 16f06302-8496-3e1d-9eda-2e3f06de8b1d | -10.7015 | -54.1663 | 2026-09-12 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 226.7 |
| 19367e56-0dd6-31e5-ac97-82537e550936 | -2.7148 | -57.6469 | 2026-09-12 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 949954d2-7fa8-355b-b274-298d21701b66 | -9.7133 | -64.9637 | 2026-09-12 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 46763c55-37c0-3737-aab7-c60bfe5813ad | -3.2128 | -46.9602 | 2026-09-12 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| ada6e8c4-e208-3cf0-bd1b-fbbd2401eeb8 | -2.7331 | -57.6465 | 2026-09-12 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 7e6063b8-d4c7-31a9-945f-603ae26945c4 | -3.2129 | -46.9383 | 2026-09-12 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 989e9434-3e4e-3b82-a948-063a4b138ab0 | -3.7462 | -61.7552 | 2026-09-12 02:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| ca4f7d69-8fe7-30ec-9626-144c18a978ca | -10.6827 | -54.1679 | 2026-09-12 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.6 |
| bf63866d-0837-3b6a-a031-f7f34cca8a82 | -5.7756 | -45.0826 | 2026-09-12 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 210.5 |
| 264f6804-d33c-313d-826f-bd9c474c1eb1 | -2.7148 | -57.6274 | 2026-09-12 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| aa99eff5-d7d9-3158-ba8e-7a5dc90316f0 | -2.97 | -50.46 | 2026-09-12 02:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8eb5d66a-3006-371c-b5ee-37e7b859dcc3 | -2.97 | -50.35 | 2026-09-12 02:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 773eabdd-1c17-37f4-b505-85e4a5b00c90 | -2.94 | -50.4 | 2026-09-12 02:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 466ec1c1-11c3-3651-816e-9e9a80a55815 | -3.23 | -46.93 | 2026-09-12 02:15:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 684a9e3a-f17b-3c16-88b5-024b2cf05682 | -2.97 | -50.4 | 2026-09-12 02:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01caaa2c-5ca6-372e-b1d2-8280118bc643 | -5.76 | -45.09 | 2026-09-12 02:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4109b38f-4300-39c9-8363-63455004f85a | -5.7569 | -45.084 | 2026-09-12 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 1ad1d85e-65f0-31db-9fa3-fb5365d2fa38 | -2.7148 | -57.6469 | 2026-09-12 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 64e7bd59-1af3-306c-b490-3347e4394547 | -4.2951 | -49.1234 | 2026-09-12 02:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| cf141707-5ba4-3ac8-a668-0aa39c724759 | -2.7331 | -57.6271 | 2026-09-12 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| b6a4f44e-64d4-389b-98b3-b4d358f5335a | -3.2313 | -46.9596 | 2026-09-12 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 201.3 |
| c46f35bf-5302-3ed1-8f8d-2d44d622ed96 | -5.7756 | -45.0826 | 2026-09-12 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 242.8 |
| 1f76c591-a287-31a1-b63f-82002007f054 | -5.7754 | -45.1053 | 2026-09-12 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 219.5 |
| 0323f133-a5c2-3e0f-9b92-67fef96d9f36 | -10.7018 | -54.1458 | 2026-09-12 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 4a8b3411-c45c-35d0-b171-52bfb8e0d22a | -10.2182 | -36.3433 | 2026-09-12 02:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 139.1 |
| 82f196b8-bf20-3360-a891-fdf89200cb76 | -10.6827 | -54.1679 | 2026-09-12 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 176.8 |
| af36a703-fab8-369e-9655-e2f8746692b4 | -3.7462 | -61.7552 | 2026-09-12 02:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| a9c86445-dd16-3f31-8665-911c7adb506e | -6.2243 | -51.6949 | 2026-09-12 02:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| ab84ae38-59ea-3348-a355-ea541f60a725 | -3.2314 | -46.9376 | 2026-09-12 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 138.0 |
| c3f16a2e-0553-3f6d-a3d9-8652e0572e5c | -6.2429 | -51.6939 | 2026-09-12 02:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 712dd6dd-c10a-3375-b0d7-a867d12b7947 | -2.7331 | -57.6465 | 2026-09-12 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 220774fc-13fc-3b00-bdd1-7c978e51f6a9 | -10.6829 | -54.1475 | 2026-09-12 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 79095e4a-b74a-3d5e-a5c3-24255a8e09d1 | -2.7148 | -57.6274 | 2026-09-12 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 4abd2ad1-44ee-3a82-ace1-99f527c59c84 | -10.7015 | -54.1663 | 2026-09-12 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 147.4 |
| 091b0281-92b2-38a8-84c2-39ee202069bb | -5.7567 | -45.1067 | 2026-09-12 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 7e161930-d277-31eb-96b1-9f65e49ef10e | -10.7015 | -54.1663 | 2026-09-12 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 148.9 |
| ba3f18d1-6f67-3a30-81de-83d6b13b86b5 | -5.7754 | -45.1053 | 2026-09-12 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 198.1 |
| 037ca701-00fc-3399-9401-643395c77ef3 | -5.7756 | -45.0826 | 2026-09-12 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 238.4 |
| 94cb190b-52b4-30c1-b82c-d566702dfdf9 | -3.7462 | -61.7552 | 2026-09-12 02:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| e2170d8e-e825-35f1-8d0f-698cc522cb61 | -10.6827 | -54.1679 | 2026-09-12 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 128.4 |
| 9c47f101-0757-3ace-8dcd-aabf0c5eb026 | -4.3587 | -47.7853 | 2026-09-12 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 5253856b-2e77-355d-a05b-cfef5c5ffb58 | -3.728 | -61.7555 | 2026-09-12 02:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 4799c8c1-031a-36be-b6ac-35d3d8571fe6 | -10.7018 | -54.1458 | 2026-09-12 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 083c778b-3f3a-33a8-9395-7bf1de6ab5fa | -6.6021 | -58.849 | 2026-09-12 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 80a708ab-a2a4-33ff-b3c9-bd6cd91566dd | -6.2429 | -51.6939 | 2026-09-12 02:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 99b5aa24-b56b-36f3-ab61-a9f2d0ace3d1 | -18.6668 | -41.9962 | 2026-09-12 02:30:00 | GOES-19 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.7 |
| ece97dad-f1f3-310e-9f3c-82c5926e2771 | -5.7567 | -45.1067 | 2026-09-12 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 1dd94ac8-3671-348b-9802-9310daf9ac03 | -2.7331 | -57.6271 | 2026-09-12 02:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 39c01110-bff6-34bd-8be0-32a7cf3dcba8 | -2.7148 | -57.6469 | 2026-09-12 02:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 2871190d-2b5c-3b82-9e59-ad17c86b5ca8 | -6.2243 | -51.6949 | 2026-09-12 02:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 3dd199f4-5f58-3668-9170-e794ec684f78 | -2.7148 | -57.6274 | 2026-09-12 02:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 25c13fad-de3b-3661-8a0b-02fa80765bce | -10.6829 | -54.1475 | 2026-09-12 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 81c33d6a-b9c8-3571-a80c-e42f6a5913a7 | -5.7569 | -45.084 | 2026-09-12 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 4b65537d-d215-3e39-bac0-04b24aeae7d5 | -2.7331 | -57.6465 | 2026-09-12 02:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| be11f6e2-a1fb-34bf-8b42-57dc58bc4623 | -3.2313 | -46.9596 | 2026-09-12 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 173.1 |
| 89273f16-d4ee-3e95-a6c1-66c301404125 | -3.2314 | -46.9376 | 2026-09-12 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 156.4 |
| 5052f045-bd11-3402-bd0c-8ceb24707a94 | -2.7148 | -57.6274 | 2026-09-12 02:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 28fceb22-d5b0-363e-b033-83b184f4da85 | -4.3587 | -47.7853 | 2026-09-12 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 5413b6ad-698a-33c9-bbe3-94d99d2913fd | -10.6827 | -54.1679 | 2026-09-12 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 145.6 |
| e5e15683-6afc-378c-8821-404177dd94d4 | -10.7015 | -54.1663 | 2026-09-12 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 2ee6acc3-0ea5-327b-829d-df04ba12f717 | -5.7569 | -45.084 | 2026-09-12 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 143.6 |
| f21811cf-6c77-3256-b66e-96f96e0ee124 | -5.7567 | -45.1067 | 2026-09-12 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| f502bdf2-3306-3a10-850a-22292eca0c89 | -6.6206 | -58.8483 | 2026-09-12 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| f445e2eb-d4f0-3d26-9bdf-c22e7f1ea77f | -6.2243 | -51.6949 | 2026-09-12 02:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 77c833d6-c18d-3da3-b76d-d554173554b0 | -5.7756 | -45.0826 | 2026-09-12 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 211.6 |
| 67224b35-67f7-33d0-a0c5-e85ccc757ade | -3.2314 | -46.9376 | 2026-09-12 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| c8bb6ce7-651c-3924-a37f-46762b62a852 | -3.2313 | -46.9596 | 2026-09-12 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 171.5 |
| 7102dac0-2a81-3a10-8db7-9c2bdefbbd03 | -10.6829 | -54.1475 | 2026-09-12 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| bceb7e1f-a802-3707-9315-9db8b232e580 | -6.6021 | -58.849 | 2026-09-12 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 624f0085-3f37-3098-a5c3-0f8e7816422d | -5.7754 | -45.1053 | 2026-09-12 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 177.0 |
| c34c4e8c-4131-3a50-aea8-2b9b98c5d5e4 | -3.728 | -61.7555 | 2026-09-12 02:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 2e6c6548-a4e5-376a-a1df-cb7415f63328 | -3.7462 | -61.7552 | 2026-09-12 02:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 840c94e7-2b4d-34aa-ab85-d0ea417a1a55 | -2.7148 | -57.6469 | 2026-09-12 02:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 324c5e6e-2937-34fd-85ac-3a4b73b53773 | -6.2429 | -51.6939 | 2026-09-12 02:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 9c736ff8-081b-3841-a8b0-2318b076298b | -2.7331 | -57.6271 | 2026-09-12 02:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 11b5ef54-f962-32bd-a3b7-0cc648a63ab8 | -2.7331 | -57.6465 | 2026-09-12 02:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| fac41de2-89b7-3b14-aa81-583e8c2bb2fa | -4.3587 | -47.7853 | 2026-09-12 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 6a857aef-7cdd-3f4f-83ea-d8cdf5f1c406 | -5.7756 | -45.0826 | 2026-09-12 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 218.7 |
| 2e05381b-507a-3cac-8e7b-6838ba4c6595 | -3.7462 | -61.7552 | 2026-09-12 02:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 734b6713-e168-33ff-8f29-b21dd096bc45 | -2.7148 | -57.6469 | 2026-09-12 02:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| d112187b-eb13-31b1-a987-8a76c1fbb946 | -10.6827 | -54.1679 | 2026-09-12 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| e51272a9-9250-36f4-a1d4-1dcdf594fb81 | -2.7148 | -57.6274 | 2026-09-12 02:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 27b35824-d82f-3842-8c88-6685ecc01ee7 | -2.7331 | -57.6465 | 2026-09-12 02:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 67ac53e2-0b11-342d-aff6-5b7dd7253514 | -18.6668 | -41.9962 | 2026-09-12 02:50:00 | GOES-19 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 121.5 |
| 5668cf9f-a79f-30fc-93cb-2e760c9317de | -5.7754 | -45.1053 | 2026-09-12 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 177.1 |
| c572cb2d-b880-3488-857e-ca6da603967c | -6.2429 | -51.6939 | 2026-09-12 02:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 641b48c7-32c8-313c-b792-845238623781 | -3.728 | -61.7555 | 2026-09-12 02:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 36c71e09-595b-39b4-9d2f-442cbb0d1b39 | -2.7331 | -57.6271 | 2026-09-12 02:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |


[Clique aqui para ver as próximas entradas](README10.md)
