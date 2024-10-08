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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d104625a-f7a1-3ced-8912-ca1047a65a35 | -9.56931 | -50.23253 | 2024-10-08 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5990792-92b4-397d-a3f6-916e30509e6f | -10.52396 | -49.11129 | 2024-10-08 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 074d27e7-35ee-3728-914a-ed128474285c | -10.52021 | -49.10677 | 2024-10-08 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 984d8392-01cf-351f-94f7-3264331b6da5 | -10.51967 | -49.11075 | 2024-10-08 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc0d080a-97db-33ac-8050-9f8eef16aba4 | -12.20474 | -50.57877 | 2024-10-08 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2615fdca-36da-3dae-8e5e-9e0bf9b04343 | -12.20076 | -50.57819 | 2024-10-08 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f0514755-8b37-3bd1-8a14-9470891e7128 | -12.11137 | -50.90166 | 2024-10-08 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5883f411-a26c-39d7-9a41-caa25bb8d22c | -12.10816 | -50.89612 | 2024-10-08 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 156c15e0-dc15-36ae-88c4-3409836393d6 | -12.10427 | -50.89555 | 2024-10-08 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae91dd63-5d9c-37d4-8588-a8f31dae6d75 | -12.08945 | -50.91709 | 2024-10-08 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7abebf95-8160-3c8b-b43d-5356baa79919 | -11.70502 | -49.95531 | 2024-10-08 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54dd151e-bc39-3f86-976d-fa98cd00e648 | -11.70451 | -49.95903 | 2024-10-08 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b649dba-cf7a-3548-96bc-b8ef25297ca6 | -11.70401 | -49.96273 | 2024-10-08 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 343c881a-0a69-3a3a-b488-1024b1b50c51 | -11.5294 | -49.82413 | 2024-10-08 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 758bdfb8-5b05-3905-aac9-022d37043120 | -11.52474 | -49.8273 | 2024-10-08 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 386f14d0-4b05-37f8-9003-c87b564496fb | -11.39503 | -50.04685 | 2024-10-08 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d12332fb-74bd-36d1-bbf8-52576ac8a88a | -11.18801 | -49.6468 | 2024-10-08 04:57:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7efdc868-bbf1-376f-83d3-ab9b80f7ed54 | -11.18467 | -49.6462 | 2024-10-08 04:57:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 07cee69c-4b9f-3354-8470-fd2d1f76526c | -11.18385 | -49.64621 | 2024-10-08 04:57:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e4077a03-a731-359f-9619-9d0e750f8bc4 | -12.81768 | -50.5434 | 2024-10-08 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8d63dea-7f96-393d-aa0e-8521b52d4af4 | -14.25064 | -51.32262 | 2024-10-08 04:57:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5954e20-27cc-3e65-aded-f34646d77f64 | -13.8897 | -51.28562 | 2024-10-08 04:57:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0faee554-30e3-323b-adee-9cd6816fdb2c | -13.88581 | -51.28502 | 2024-10-08 04:57:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7521eeeb-bebd-3586-90b7-ae56434746e9 | -15.07745 | -51.23722 | 2024-10-08 04:57:00 | NPP-375D | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ba962c18-4a6b-3f12-90de-b1c45cf8e1d1 | -15.07278 | -51.24188 | 2024-10-08 04:57:00 | NPP-375D | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f77c3fc-b8c5-341a-a750-00a668907b6f | -15.06226 | -51.22967 | 2024-10-08 04:57:00 | NPP-375D | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb3cd64e-bd4d-339f-b65d-4043aa75238a | -15.06067 | -51.22812 | 2024-10-08 04:57:00 | NPP-375D | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04ee8842-a3bc-38c1-9d15-91b1a961d569 | -15.04368 | -51.26287 | 2024-10-08 04:57:00 | NPP-375D | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 941914e6-3964-31f8-abc4-f1cc88868642 | -14.80952 | -50.80338 | 2024-10-08 04:57:00 | NPP-375D | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 060d8229-7528-3e88-9809-3de0b2b2457c | -14.79711 | -50.7716 | 2024-10-08 04:57:00 | NPP-375D | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f798f74-514f-3e35-b529-3067155c77eb | -14.79663 | -50.77528 | 2024-10-08 04:57:00 | NPP-375D | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 558032ed-d833-3838-b90a-fa20590f1330 | -10.61533 | -50.91464 | 2024-10-08 04:57:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 690e44a7-6d0b-3927-ab05-91f2e399038b | -10.61465 | -50.91934 | 2024-10-08 04:57:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5aa04d9e-a9b6-3cac-bbc5-122a214f013a | -11.9869 | -51.91626 | 2024-10-08 04:57:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a03cba3-5e6c-31f1-8e0c-4dfe1ead146a | -11.98323 | -51.91574 | 2024-10-08 04:57:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a52e4d1e-d8a2-3734-924a-d2ac16c23aed | -11.97955 | -51.91523 | 2024-10-08 04:57:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d199eee-3963-38a4-bc0e-3d6faf753b0f | -11.33029 | -51.07853 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bbbd8f9-59a4-33e6-bf8e-8a2aec2c2593 | -11.32964 | -50.98419 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92909758-e70f-35a1-8dac-8d32c33b4316 | -11.32834 | -50.98109 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc9ee393-5749-38d3-a752-cdd96874d6ce | -11.32647 | -51.07796 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 007e2f7a-746b-360e-b5a9-04f9f02f2e04 | -11.3258 | -51.08269 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0b87261-0157-3984-8f27-a9a62b5b805d | -11.3258 | -50.98363 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 252e5023-e792-3150-af3e-0c92b00ac43e | -11.3245 | -50.98053 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 740cbc2f-30df-3970-9108-102ad30a7923 | -11.32412 | -51.33881 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| adf94f46-5fc9-367d-bd12-0497f6deba9e | -11.32347 | -51.34338 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a50e35d0-8363-32d2-8379-7bd2a109c6df | -11.32199 | -51.08213 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac2b0e48-cd2e-38c3-a35f-de8aa7725fc6 | -11.31971 | -51.34282 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38956fab-04c9-39a7-984d-192469cc73f7 | -11.31817 | -51.08156 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba3379ca-d68d-3350-899f-f5ecc52b75d7 | -11.31436 | -51.081 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4687fd4-5061-34a9-a1dc-755d1c4312e2 | -11.31268 | -51.0372 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45dd9e2b-4337-31f2-9f18-a6d48888ab3b | -11.31084 | -51.05912 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8677f624-3dff-3e35-b160-173fa5a8b8aa | -11.31048 | -51.03486 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7e4ed5f-2e93-3dee-a6b4-f546dc881ea5 | -11.31045 | -50.98139 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddb67c6e-7397-3b89-954f-b6ff464a0b03 | -11.31003 | -51.05621 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43294052-3b72-34ce-a03a-ed12102b755f | -11.3091 | -51.04435 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ef2fd31-fefb-3c91-87d2-6733ef5e08bc | -11.30805 | -51.07041 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 796395f9-3464-39f6-8ff4-790a753ef451 | -11.30753 | -51.04614 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82d91b94-09b6-3d48-89a4-8608c3fea516 | -11.30702 | -51.05858 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 80fa30e5-d4fd-3487-b84f-fdcab2ffbab6 | -11.30633 | -51.06331 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 87ffad7f-03a1-3002-9708-f28c0fffc001 | -11.30597 | -51.03905 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2440ddd8-7654-3855-834c-2638c882ad0c | -11.30564 | -51.06802 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6cf502ea-f673-3029-a103-553ed1b60cd2 | -11.30555 | -51.0604 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b94cf4d4-d861-3400-a555-1a28cfc2942f | -11.30527 | -51.04379 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 128b9551-253e-3cf8-b13a-c99c804432df | -11.30495 | -51.07274 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9061dabd-6c22-3fc4-a93b-638bb8d5b4f9 | -11.30491 | -51.01949 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6701f290-0ba5-365a-a443-95d3409c136b | -11.30489 | -51.06513 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b30ec116-841a-372a-b912-92f6c9955d0c | -11.30423 | -51.06985 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 37079e64-00df-3e7e-a9e0-35f263e89e61 | -11.30357 | -51.07458 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7f4d41a0-80bb-3a04-a67e-c9afe9794211 | -11.30251 | -51.06276 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d5dc03f-ea5b-3a40-a44a-9545d4c376da | -11.30182 | -51.06747 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3cd4946d-dc0e-39eb-86b7-07cbceb32d60 | -11.30113 | -51.07219 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 44233207-c48c-3e76-8ceb-ec8b3710faf7 | -11.30108 | -51.01892 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47876427-c5f6-3805-82ef-a2c82596a1d3 | -11.30092 | -51.34002 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9720153-bf19-3bb9-9a35-86427621aa00 | -11.298 | -51.06692 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4044d5d9-aaa1-3fa6-aa58-8be94e472abd | -11.29731 | -51.07164 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1cd3f928-d702-368a-b630-40b709c7ff2e | -11.2667 | -51.41163 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 986c0629-8608-386d-b489-0e9a28f80a1d | -11.25849 | -51.28474 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e07c2b89-dada-3abe-9975-fc78809363c4 | -11.25515 | -51.30762 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eac0a404-8a22-3fdf-a693-6b8dd4b6017d | -11.25473 | -51.28418 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 432ae593-3331-3810-be1e-bc32fe6cb725 | -11.24343 | -51.28248 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21da8d76-95c2-3c05-95e0-e4defbfc6330 | -11.21939 | -51.39534 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ca54e72-f7f7-3713-b7a2-8b78a5c99737 | -11.21322 | -51.38517 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcc871d3-578d-3ae7-8fdf-b933319a6fa8 | -11.21256 | -51.3897 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8513d37-0fbc-3f80-b7ed-99a8a58fdf45 | -11.20947 | -51.38461 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 52e254f4-dce9-3abf-843b-4357985d9076 | -11.20882 | -51.38914 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1100206b-00a3-371e-9b98-b5589264943a | -11.20638 | -51.37951 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d36e2fc-3b27-3b74-936c-c3ccc6b8fcb2 | -11.20573 | -51.38404 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 82038c77-439b-326a-9d68-d0f191d60562 | -11.20394 | -51.36988 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de791662-77e6-3d22-9b3b-fae91fa365ee | -11.20329 | -51.37442 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 508d4084-56f4-3bf6-bd6b-3cac54130403 | -11.20264 | -51.37896 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9721cedc-70bb-322b-a387-8ed7b9dedfcc | -11.2015 | -51.36025 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c0341bd-9cc5-3e5a-9d22-51f32dc16c7a | -11.20085 | -51.36478 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0223ce13-e8e1-3df0-8dd9-6b940eac40d8 | -11.2002 | -51.36934 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bac4c0e0-0544-3fa5-b522-f8a6f8bbb394 | -13.13376 | -51.64202 | 2024-10-08 04:57:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0011a6f-ea5a-39bc-a23b-6481999d4b58 | -13.1293 | -51.6462 | 2024-10-08 04:57:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c35abfe9-f02e-316b-b9bc-dc84870bec00 | -12.6337 | -52.43363 | 2024-10-08 04:57:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ac5257f-83d1-311f-8895-bc1b5ef3ff07 | -12.6301 | -52.43307 | 2024-10-08 04:57:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 84794c33-ac12-33ac-bffb-c047f0042a41 | -8.97748 | -52.79936 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58ef3c12-ad4a-3c43-9e4e-724af0635b8e | -8.97235 | -52.78701 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef954075-fbc5-3d29-bfa5-bbd28d51eb8c | -8.97177 | -52.79081 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README86.md)
