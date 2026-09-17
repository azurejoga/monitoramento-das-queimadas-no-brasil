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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d849d93a-baf2-3d7b-a25a-4205833b47d2 | -8.4796 | -57.6478 | 2026-09-17 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 197.6 |
| 8ef05f3b-2412-3302-875d-a9fcc5bc4a36 | -15.5715 | -54.223 | 2026-09-17 15:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| c4913310-65ba-3d6f-b245-b0aac8c4e57f | -8.4669 | -44.5445 | 2026-09-17 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 7244c6d6-3bbf-3523-b393-9438e68f6ff2 | -9.769 | -46.0841 | 2026-09-17 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 157.7 |
| fded6fa6-9c3c-3454-884d-0693d118586b | -12.7709 | -51.2403 | 2026-09-17 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 811d7df4-d2a7-35d0-a5ce-2f49bd9af180 | -13.299 | -51.7288 | 2026-09-17 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 91acbfd8-9bc3-387d-86a6-eb4727c3deb3 | -13.2047 | -51.6342 | 2026-09-17 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 44dd654d-de77-334e-97e5-a3e2229a62c6 | -9.0866 | -61.0287 | 2026-09-17 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| f13a6eca-58d2-351d-9dc4-fcb5569d220e | -8.5998 | -44.4839 | 2026-09-17 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 6d349bd5-1216-34cb-84d8-bb3c36f0e99e | -9.3577 | -50.0943 | 2026-09-17 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| d7957dd6-36d5-3414-b529-c03031401c8e | -13.2986 | -51.7501 | 2026-09-17 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 030285a4-1d2d-30b2-8b2a-48d398c70583 | -9.3803 | -46.8455 | 2026-09-17 15:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 161.3 |
| a877eea4-f8c5-3a46-b9bc-cdfcc0d4633d | -13.205 | -51.6129 | 2026-09-17 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 989fb5e0-a6aa-3f7c-9030-6a959f677667 | -14.2796 | -51.7097 | 2026-09-17 15:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 042cc5e0-2f34-37c1-bbe3-1743c74d5c01 | -9.7497 | -46.1089 | 2026-09-17 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.1 |
| ce4830bc-d3ad-3387-9771-dec7930fe626 | -7.841 | -44.8614 | 2026-09-17 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 39af29af-58b7-34e1-81c6-b9df431180c3 | -9.9143 | -46.5172 | 2026-09-17 15:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 5d8c6931-ea50-383d-85d0-21534a4dc076 | -9.7608 | -60.4561 | 2026-09-17 15:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| c6cecc92-7d3b-3316-9b3c-826e23a7c112 | -6.67 | -43.657 | 2026-09-17 15:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 98b50292-104f-3ce8-95dd-af2bb48ab155 | -7.0428 | -59.2173 | 2026-09-17 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 41ae3fc6-688c-3f55-88f1-f8a14199a82a | -6.6021 | -58.849 | 2026-09-17 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 218fb78a-65fc-377c-b02d-ef8f56957dee | -11.2113 | -54.1208 | 2026-09-17 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| b81578d8-d508-3a5d-a1f5-101714a14d5d | -9.3765 | -50.0925 | 2026-09-17 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 56327fb0-c73f-3143-a6da-daa4ab47ed87 | -13.3758 | -51.7193 | 2026-09-17 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 1f8c475f-f6a8-3ade-89c3-0ea559370c16 | -7.0242 | -59.2374 | 2026-09-17 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 45cd3637-e040-329d-9dd2-a126aa94dc34 | -10.6525 | -50.5631 | 2026-09-17 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 7fce509f-e3db-3339-8974-67a51af646b7 | -6.5836 | -58.8691 | 2026-09-17 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 243e177b-6453-379c-bedf-2d8089224d24 | -11.875 | -47.5902 | 2026-09-17 15:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| e1840bc1-cd33-30da-af82-39bba1699678 | -11.2488 | -54.1378 | 2026-09-17 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 64dac6ef-9981-3e00-b10f-3a676c28c4ec | -4.5045 | -54.9646 | 2026-09-17 15:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 150.1 |
| c41b0e2a-7683-3f25-907d-0fa43fea1fe9 | -9.3763 | -50.1139 | 2026-09-17 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 40ae040b-2f9b-38b4-a5ce-5497396cb818 | -1.4578 | -54.2166 | 2026-09-17 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| f49caae2-5cde-35a7-b361-7c8cce7bceb6 | -6.583 | -58.9658 | 2026-09-17 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 9cac3830-f88e-3e07-bec0-e860a0d2339b | -11.3629 | -44.0112 | 2026-09-17 15:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 0e7f45de-5b65-3d71-a148-4fc9a15c9e6b | -8.4797 | -57.6282 | 2026-09-17 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 149.0 |
| 87d95f37-e13d-3675-862d-817aa89d3727 | -11.1924 | -54.1225 | 2026-09-17 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| cfd66b12-010b-3993-b44d-f0e3b2c121ab | -7.6414 | -45.8556 | 2026-09-17 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 6492fe33-4026-33cb-bdc6-bfa7ca73c734 | -12.3384 | -50.8228 | 2026-09-17 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 31169d87-b72d-3b67-b836-7cde2cc1ea50 | -13.6531 | -45.97 | 2026-09-17 15:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| a40b7871-8b86-382f-8308-9a894c654338 | -8.0748 | -54.8499 | 2026-09-17 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 289244bd-4346-3efc-8b8e-dbd071b0aecd | -6.7648 | -59.4408 | 2026-09-17 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| c90112a3-7d01-3161-829f-36150f494077 | -12.0273 | -49.9799 | 2026-09-17 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| cfd10750-f34c-317b-8592-1794455d79a7 | -8.9412 | -44.3995 | 2026-09-17 15:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 174.4 |
| dc4cbc8b-555b-399c-9ff5-8c56adb6c826 | -11.8928 | -50.0608 | 2026-09-17 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| e0462143-893e-36b9-9e34-0540df4e5ef7 | -11.2488 | -54.1378 | 2026-09-17 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| a51c152d-abd7-360f-9e55-fb747c9be6a8 | -15.539 | -53.8502 | 2026-09-17 15:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| cfe874b3-5539-32e6-ab7b-b77b785cddc7 | -8.4797 | -57.6282 | 2026-09-17 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 158.2 |
| 8560d685-d14a-3656-86f9-5602d48d3f7b | -7.8601 | -44.8366 | 2026-09-17 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 22a79d46-b239-3674-85db-8818efcd9ad6 | -13.299 | -51.7288 | 2026-09-17 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 2089b26a-7ae3-31bb-8990-9c2e315a77a1 | -13.3182 | -51.7264 | 2026-09-17 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| f7b5cf3d-cdff-364d-8b23-49e5cf80b8d9 | -6.0256 | -59.9293 | 2026-09-17 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 49ecf708-2f7d-3836-8b5d-d8bacbb21bab | -9.1052 | -61.0278 | 2026-09-17 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| c8ed7166-cf96-3ac2-8347-0812a1e0500e | -8.5611 | -44.5573 | 2026-09-17 15:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 89a97c08-dc8c-3561-b335-cf42dd51a8a7 | -15.5715 | -54.223 | 2026-09-17 15:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| bf7f3acc-dc20-3386-becd-e7f08d12b61f | -12.0905 | -50.8307 | 2026-09-17 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 0bbc1f91-eddb-3af8-ba0c-4a7486866ae8 | -8.5239 | -44.5153 | 2026-09-17 15:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 136.6 |
| e101c5f0-8d41-312c-8122-b6950a227ca2 | -8.9108 | -62.391 | 2026-09-17 15:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 7d1d3006-0e3a-39b1-9dbe-9ffaa3d4f8dd | -7.0428 | -59.2173 | 2026-09-17 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 3d4d1849-82a5-3086-9875-b81026790066 | -6.5837 | -58.8498 | 2026-09-17 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| b336dac8-9d14-3cdd-b421-5a7ec1bf300c | -7.0612 | -59.2358 | 2026-09-17 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 78ab3ca9-a633-3899-902c-27a7afb2a84c | -7.9543 | -44.8273 | 2026-09-17 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 81b94080-122b-3717-b024-37a1a6a2863c | -9.7979 | -60.4734 | 2026-09-17 15:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 8935fbc8-0e54-3a5b-8e06-9b7a6f918606 | -9.7687 | -46.1067 | 2026-09-17 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 8f21daa3-5172-3944-a74a-c859902bfd7c | -12.7709 | -51.2403 | 2026-09-17 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| d720ad39-be8b-33bc-88a0-a25b4eb40fbb | -9.8322 | -48.3417 | 2026-09-17 15:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 302.3 |
| 0c5557d7-7413-3530-903f-b8075c3f19ed | -6.6766 | -58.7299 | 2026-09-17 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 8c9b5af3-f6d1-35ae-a684-c0eb3dc41758 | -8.9294 | -62.3902 | 2026-09-17 15:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 01169ccf-6094-38ad-a38d-dab07050d57c | -9.0866 | -61.0287 | 2026-09-17 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 75ff8153-ac20-3654-9063-68ba777d7837 | -11.875 | -47.5902 | 2026-09-17 15:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| b3cef4b0-8a2f-3142-ba77-b0f771bd02d7 | -13.1855 | -51.6365 | 2026-09-17 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 9280b91b-e9e3-3b0a-9ed0-f40d8f141dbe | -6.0196 | -51.7893 | 2026-09-17 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| a61380d1-6ede-3f2c-ac3e-f15141b35cc0 | -11.2115 | -54.1003 | 2026-09-17 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| b1ce8e02-eaa5-35ac-80b4-1a8d80de735f | -7.0613 | -59.2165 | 2026-09-17 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| cac53bc7-7372-3162-846e-deb9efd40646 | -15.5386 | -53.8712 | 2026-09-17 15:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 71e33911-29d4-3ec8-92b0-89f59da0e3b2 | -13.3754 | -51.7406 | 2026-09-17 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 5c797638-02e8-3e12-8787-1d671fd41dde | -15.5584 | -53.8477 | 2026-09-17 15:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 4517d1e2-1919-35c4-87ef-503ab9a6a2bd | -7.8221 | -44.8632 | 2026-09-17 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.2 |
| c8b6344d-e90a-3e01-9db0-a03ecb8f2a87 | -7.0242 | -59.2374 | 2026-09-17 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 1066cc3d-762a-3aa2-8b9c-5ff7b5c69063 | -13.2047 | -51.6342 | 2026-09-17 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| aa7bfe85-89f0-3bfc-a81e-dafb1e466814 | -12.0464 | -49.9776 | 2026-09-17 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| bab2c12b-7618-34fa-8e55-bc43cc7b2efb | -6.583 | -58.9658 | 2026-09-17 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 1c24fb62-694b-37dc-9a4f-e97b93b56074 | -9.3954 | -50.0908 | 2026-09-17 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 6734c25f-7ada-3b98-9c6c-a6f7ebbeaefe | -9.3577 | -50.0943 | 2026-09-17 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 463a330e-b04f-3d01-bba6-075264f96172 | -4.5229 | -54.9639 | 2026-09-17 15:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 134.9 |
| bc7f9a4a-b51f-3bcf-b5a1-9524529f17b5 | -7.6417 | -45.8331 | 2026-09-17 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 3d117bc8-327a-3c5e-843c-eb3a195d6978 | -11.3161 | -46.7699 | 2026-09-17 15:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 541a1ccc-9b5e-36e3-8175-1a4122b40710 | -14.8183 | -59.5532 | 2026-09-17 15:20:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| f1823758-c896-396c-934c-73c485c72ab4 | -9.769 | -46.0841 | 2026-09-17 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 192.4 |
| 8f4157ae-1717-308f-9604-df8197086928 | -9.3765 | -50.0925 | 2026-09-17 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 33bbab19-2e00-38b7-874f-f02bc54ed559 | -11.8924 | -50.0823 | 2026-09-17 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 6a2dcd76-967b-3d28-b0b3-41de47f52fd6 | -9.3569 | -50.1583 | 2026-09-17 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| a3990bf0-5ca2-3d81-842b-ff35a5752f7b | -8.4983 | -57.6271 | 2026-09-17 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 224.2 |
| dee4e5ae-e187-3c84-bf11-ffd072e366f2 | -7.0849 | -45.2505 | 2026-09-17 15:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 1c337461-aa63-39c6-bcd3-d24cbd8cd72d | -6.6765 | -58.7492 | 2026-09-17 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 80c7033c-a230-3061-98fa-59417d15e6d8 | -6.67 | -43.657 | 2026-09-17 15:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 546653e9-f4f2-3290-8a55-4e88bbf03ce8 | -13.2239 | -51.6318 | 2026-09-17 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| ed57ac70-8e9c-3459-8e05-ebd969ffb6cf | -6.6703 | -43.6337 | 2026-09-17 15:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 34633c89-87be-31bf-8e6d-ce7dc8ffc4f9 | -8.5797 | -44.5783 | 2026-09-17 15:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 4b192ab7-03cf-3e2b-88a9-7827bdebaa11 | 1.0583 | -50.999 | 2026-09-17 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 8c740e0f-6a78-3ad9-b651-b0b306104568 | -8.8647 | -45.8693 | 2026-09-17 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.2 |


[Clique aqui para ver as próximas entradas](README98.md)
