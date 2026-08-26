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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b4c66c9-9aee-368b-b24c-c8c32f2a6c54 | -13.2476 | -51.3521 | 2026-08-26 07:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 5d76d809-19f9-3380-9740-e4d57a535b9a | -6.641 | -58.4987 | 2026-08-26 07:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| c370f56e-069d-3561-bf3a-56b43c70dc07 | -12.6644 | -48.4142 | 2026-08-26 07:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 11f31b38-6cf6-3546-86d5-20cc66c978cb | -13.1906 | -51.3166 | 2026-08-26 07:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 3236b868-5f0b-30c7-9f50-0fd110fca83d | -13.1715 | -51.319 | 2026-08-26 07:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 10624a2e-e292-3e2c-b9a9-e041b3a1f38e | -13.2287 | -51.3332 | 2026-08-26 07:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| c09d4c2e-b394-322d-ba8f-c3c118c4abba | -7.5104 | -61.3832 | 2026-08-26 07:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 1798ebe4-8c94-3bda-a316-47eff45d4971 | -9.6024 | -55.1078 | 2026-08-26 07:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 377612ff-9c11-31b1-a9f4-7bfb9737c206 | -13.2476 | -51.3521 | 2026-08-26 07:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 89951e6d-c933-3c26-ac0c-bf965579c8a2 | -13.2479 | -51.3308 | 2026-08-26 07:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| e56fcc6d-8520-3f19-847b-c314e0cc76c7 | -7.5104 | -61.3832 | 2026-08-26 07:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 816d8edd-186f-3af1-9859-58e8effb2ac8 | -13.2098 | -51.3142 | 2026-08-26 07:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| bc16effa-d82b-3eca-bcd3-56185c4dfc99 | -13.1906 | -51.3166 | 2026-08-26 07:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 196.0 |
| 782e20f4-0b11-343c-b2a9-520c846a180b | -13.2668 | -51.3497 | 2026-08-26 07:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| f9826c06-aad7-37b2-8ee2-4a53564d18d7 | -10.7598 | -54.0179 | 2026-08-26 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| ecb4e8d4-5b52-36b7-8694-ae89d0031c7b | -7.5289 | -61.3825 | 2026-08-26 07:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| b1722d4a-b52f-3274-9fd3-61bf91e64358 | -12.0358 | -46.0146 | 2026-08-26 07:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| c8ae4e29-5db6-3b58-9f13-4ab23b696fee | -13.191 | -51.2952 | 2026-08-26 07:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 5c130542-dfc6-3109-862b-2eed5e7cfc2d | -12.6644 | -48.4142 | 2026-08-26 07:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| f505b886-805d-38a2-990e-254785eca8f2 | -13.2284 | -51.3545 | 2026-08-26 07:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| f3860a2c-c9dc-3b18-82b3-f801de2fbcd9 | -13.1715 | -51.319 | 2026-08-26 07:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 69a41e93-39f9-37ac-8e3f-810b52f48be2 | -6.641 | -58.4987 | 2026-08-26 07:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| e4cc446a-7e33-3971-8950-145386c00d39 | -10.7596 | -54.0384 | 2026-08-26 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| f2059fdd-5ec2-3884-97d6-3f3417e5c846 | -10.7598 | -54.0179 | 2026-08-26 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 5a108b90-e3e8-3ed1-a3ff-243aa83129b7 | -13.2671 | -51.3284 | 2026-08-26 07:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| e72e88e9-f8af-33c0-a572-6177980db6d0 | -12.684 | -48.3894 | 2026-08-26 07:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 4da118a2-6e74-3ddc-9c87-677502ca5d81 | -13.1906 | -51.3166 | 2026-08-26 07:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| d3ee56a2-c32c-3d39-b660-f236fd006b38 | -12.6644 | -48.4142 | 2026-08-26 07:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| de5ab6b5-2c82-37a9-8f5a-98bc4a88264d | -13.2476 | -51.3521 | 2026-08-26 07:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 9311269e-8284-3dc3-a7e2-0c3761ca0d6a | -7.5289 | -61.3825 | 2026-08-26 07:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 3b5406b3-c100-3814-83ff-c933fa2e7c2d | -12.6836 | -48.4116 | 2026-08-26 07:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 7fb46d59-5342-321a-8c1e-2bdb78dca8b1 | -10.7596 | -54.0384 | 2026-08-26 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 50f06d94-e12f-3b1d-a8d7-51f0b700071a | -9.6024 | -55.1078 | 2026-08-26 07:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| cb672cea-f7ff-311f-a0d7-070847047de1 | -6.641 | -58.4987 | 2026-08-26 07:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 2ffebc98-1e88-39e1-b25f-d39f1db8d185 | -13.2668 | -51.3497 | 2026-08-26 07:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 131.5 |
| dd2ce278-b4c6-3e18-9050-128f762d4aa1 | -13.2479 | -51.3308 | 2026-08-26 07:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| f4967b7a-10e7-3a40-bdf3-423bf0cce057 | -7.5104 | -61.3832 | 2026-08-26 07:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 1664d084-48ea-300e-9e07-6dac89a49995 | -13.2284 | -51.3545 | 2026-08-26 07:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 14f9b4f9-1180-3928-bdf9-99526357b538 | -13.2668 | -51.3497 | 2026-08-26 07:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 12e4bce3-9834-3e2f-ab57-edae53f66192 | -7.5289 | -61.3825 | 2026-08-26 07:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 29c101a2-a785-3d0e-af5d-df2fa87893a9 | -13.191 | -51.2952 | 2026-08-26 07:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 67163774-184c-3977-b9f8-00b743d26d5f | -12.6836 | -48.4116 | 2026-08-26 07:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| eb62065a-5ee6-3ff6-89d0-d2ca02f968c1 | -10.7784 | -54.0368 | 2026-08-26 07:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b4983e1d-7894-313c-9711-58843a477b61 | -6.641 | -58.4987 | 2026-08-26 07:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 571c0495-e224-3f06-ad56-b545cbc2463d | -10.7596 | -54.0384 | 2026-08-26 07:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| ec7f4820-53a0-3347-acb6-437db147ba2c | -13.1906 | -51.3166 | 2026-08-26 07:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 132.0 |
| b9908207-cf26-3753-80cf-4ffcabc78dcf | -12.6644 | -48.4142 | 2026-08-26 07:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 809f3550-dfff-336a-926c-97471e988bdf | -13.2476 | -51.3521 | 2026-08-26 07:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| eb5d70c5-763e-3c54-9304-0c2dee4bdc18 | -13.2284 | -51.3545 | 2026-08-26 07:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 7cebb292-d8a1-31f1-a474-c9e4634da32a | -13.191 | -51.2952 | 2026-08-26 08:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 48ec279f-5eb0-3f8f-a3e6-d13521b266cc | -9.6024 | -55.1078 | 2026-08-26 08:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 90f6a86d-598a-3375-ae7f-a3a800a3ea39 | -13.1906 | -51.3166 | 2026-08-26 08:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 127.3 |
| e6afc0e0-48c7-371c-b5a0-0a293cb422cc | -10.7596 | -54.0384 | 2026-08-26 08:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| c84db5f3-6214-364e-9e73-38b2db4c6271 | -6.641 | -58.4987 | 2026-08-26 08:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 4e79c7c9-2b38-3896-b039-5d687ba409f1 | -7.5289 | -61.3825 | 2026-08-26 08:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 5d372dda-855f-3d3e-9c7c-00cdbd96e91c | -12.6836 | -48.4116 | 2026-08-26 08:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| a5f74e46-b70e-3d3c-b8b8-0c165d5f8a9c | -13.2092 | -51.3569 | 2026-08-26 08:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 311c01eb-c096-3948-8a41-7e59c2bae3db | -13.2284 | -51.3545 | 2026-08-26 08:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 811e16ae-c08d-3d89-80e5-77ed9430cb0b | -12.6644 | -48.4142 | 2026-08-26 08:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| ba9e6ea4-42ec-3094-a5fd-bbce0965b82f | -7.5289 | -61.3825 | 2026-08-26 08:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 3243bfbb-3cd1-3213-b863-e74e976ef3c3 | -12.6644 | -48.4142 | 2026-08-26 08:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 923d33c6-189a-3dcf-a8ed-267a6d84daa0 | -13.1906 | -51.3166 | 2026-08-26 08:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| bcc0bd83-2023-3b90-b39c-74e33b7f96fb | -10.7596 | -54.0384 | 2026-08-26 08:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| fce111b4-9a8e-3ed0-8c02-df6a1d2b9c15 | -6.641 | -58.4987 | 2026-08-26 08:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 40dc273b-0a53-3b21-ac10-0323dd8b0737 | -12.6836 | -48.4116 | 2026-08-26 08:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| b9430e49-7a44-3937-8309-f718de68d889 | -12.6644 | -48.4142 | 2026-08-26 08:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 5f0bea5e-32ab-32e1-bd34-aba5f492d2a4 | -6.641 | -58.4987 | 2026-08-26 08:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| d63cda59-13e9-389c-9b96-fed20cc10024 | -10.7784 | -54.0368 | 2026-08-26 08:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 3fc0ccc1-fc0b-379b-a37b-72732f2e73b5 | -7.5289 | -61.3825 | 2026-08-26 08:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 1d110567-4203-32f0-ab3e-089464e50823 | -13.1906 | -51.3166 | 2026-08-26 08:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 143.8 |
| b423e24f-8dc1-3a99-b2da-475033da8be7 | -12.6836 | -48.4116 | 2026-08-26 08:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 901aa4a7-15bd-3c63-9203-3543f352a5d3 | -13.191 | -51.2952 | 2026-08-26 08:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| c9affeb6-4da2-3d61-adea-e4765d729932 | -10.7596 | -54.0384 | 2026-08-26 08:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 39302502-d7a6-38fd-bda8-49020ba984d1 | -9.6212 | -55.1064 | 2026-08-26 08:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 85906478-0e48-3ae6-bcb5-5124c5e89999 | -13.2098 | -51.3142 | 2026-08-26 08:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| f7f07458-cb68-30f5-b85f-f5a64b9aa7e4 | -10.7784 | -54.0368 | 2026-08-26 08:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 9e4d16c9-4cf7-3783-8fac-02913aef1be0 | -13.1903 | -51.338 | 2026-08-26 08:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| e90bc6db-0446-3e54-b2ab-95338f0b17c3 | -12.6644 | -48.4142 | 2026-08-26 08:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 9dbfc7fe-9512-35bf-a79d-5a7fca60f149 | -10.7596 | -54.0384 | 2026-08-26 08:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| e83c16a2-bd63-3309-9d2a-8138591fa758 | -6.641 | -58.4987 | 2026-08-26 08:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 9fc0ce16-52ab-3077-8785-b8dbe8751bc1 | -9.6024 | -55.1078 | 2026-08-26 08:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| e7eb618f-459f-3808-9a53-d26651d8c6f4 | -13.191 | -51.2952 | 2026-08-26 08:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 135.8 |
| c3468542-6d3c-374f-8925-8b21e49ce4af | -13.1906 | -51.3166 | 2026-08-26 08:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 230.4 |
| 0608dd7d-4f31-3498-a83c-efee032ff0d1 | -12.6836 | -48.4116 | 2026-08-26 08:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 9683c79f-81b2-38c6-b26d-42a9439b2bc5 | -7.5289 | -61.3825 | 2026-08-26 08:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 62d46ad2-12ce-375c-b19a-2e7b24d94b13 | -10.7596 | -54.0384 | 2026-08-26 08:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| ffacd1ac-2a32-34da-a7f3-32a6985ff744 | -12.6644 | -48.4142 | 2026-08-26 08:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| b31b7967-065d-3b5a-b647-c676676fa605 | -9.6024 | -55.1078 | 2026-08-26 08:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 62eba5fd-b3a8-35b1-93b5-47fddcc2232d | -6.641 | -58.4987 | 2026-08-26 08:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 62dee7ff-adf0-3b43-87ae-47b0dfd0ace9 | -12.6836 | -48.4116 | 2026-08-26 08:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 8f988bc2-72be-30a9-9f43-894611f87f44 | -7.5289 | -61.3825 | 2026-08-26 08:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| ef0f2bf3-e6bb-3256-9722-1dcc57ab1e47 | -10.7596 | -54.0384 | 2026-08-26 08:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 85c72934-ba26-30bd-9fe3-db40f49e8cb8 | -9.6024 | -55.1078 | 2026-08-26 08:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 2a2d0b10-3380-3f0b-b7ce-94e25242693c | -6.641 | -58.4987 | 2026-08-26 08:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 7f43231a-5fd4-3a18-a32a-a71f4742b0c8 | -10.7596 | -54.0384 | 2026-08-26 09:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| b237faca-539e-329c-aabe-9df7dd229580 | -6.641 | -58.4987 | 2026-08-26 09:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 6a5247fa-ad52-330f-8ba0-b6011a45f4be | -9.6212 | -55.1064 | 2026-08-26 09:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 67efb44b-14d7-3bc1-8c62-1a9cbe79ce34 | -9.6024 | -55.1078 | 2026-08-26 09:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 813d07ef-748d-3503-9780-a935a9de878b | -7.5289 | -61.3825 | 2026-08-26 09:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 4aa93e23-da09-3947-b424-3877d293b7c0 | -6.641 | -58.4987 | 2026-08-26 09:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |


[Clique aqui para ver as próximas entradas](README77.md)
