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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1148e0dd-c425-3311-9291-a7b9f19f4618 | -11.08162 | -52.52523 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0e5cbf4a-b8f0-3da1-adff-df229dffa0af | -11.08106 | -52.52883 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a41519d3-7fb7-3310-a07f-bd3bb44d09cb | -11.07825 | -52.52471 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9bbc5f2b-a781-3ce0-bff4-79a47a1c9bf9 | -11.0777 | -52.5283 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 29745b4e-215f-3dba-8699-10ebfeff8dd3 | -11.07489 | -52.52418 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7fcde37a-e3e3-303e-969a-d5928a069ed7 | -11.07434 | -52.52777 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 37f6aeda-87d8-3a9b-a2cb-5c30cfcb6f44 | -11.07153 | -52.52365 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7d482ccb-ed61-3024-ad50-310825fb6edb | -11.07098 | -52.52724 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b281358f-1fc5-381d-aaf9-63350b2e83b7 | -11.06872 | -52.51954 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8bbed58-7d28-3e23-bf9b-b5a979e48760 | -11.06817 | -52.52312 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fdc90640-b873-3ee7-b643-d52541960fbe | -11.06481 | -52.52259 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76d8e1e8-ae8a-30c0-b111-6619c3cb52c8 | -11.06145 | -52.52205 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 88819cf8-3cea-3a5d-82a2-a88e22717222 | -11.05749 | -52.50302 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f06d210-8300-3f2e-8b6a-2d737d062a74 | -11.05413 | -52.50249 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85c72d34-8d77-32eb-b51d-ffd00c2c9254 | -11.05076 | -52.50196 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10573ecf-55ca-3a39-aafd-28ff767e5c27 | -11.05021 | -52.50555 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26879cfa-f387-3380-9bf7-d49dd5a893f7 | -11.0474 | -52.50142 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d97aa478-6c3b-3c15-988a-cfd4de527f19 | -11.04404 | -52.50089 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b3e23be-b6d4-358f-8712-d2083eb7983c | -11.04178 | -52.49316 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 725f631f-7f52-336c-ad22-4e28e6d5d032 | -11.04123 | -52.49676 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87611c7d-934d-3f5e-a5da-bab817c95df9 | -11.72387 | -52.93684 | 2024-10-03 04:51:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df807039-967c-392c-90bc-9eda7fbb7f20 | -10.8191 | -53.73396 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed14df73-7fd5-3b1e-9eba-a2ceac196f52 | -10.81577 | -53.73342 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a099cb5-4fb1-3692-ae66-19a08cf505a0 | -10.81189 | -53.7364 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 52900b10-0140-3f56-aeb3-96075e0cae56 | -13.78683 | -53.08281 | 2024-10-03 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a982a54d-ed37-35e4-831d-3e0d2c14dd7e | -13.78457 | -53.075 | 2024-10-03 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 287e992e-abf4-3a80-936d-1ab9804f1e69 | -12.6704 | -53.19651 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6795a283-394f-3b37-94a9-5e48ceb60caa | -12.66985 | -53.20009 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50196c61-0714-3c4c-b338-fa6b1a8b4f1d | -12.66706 | -53.19598 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68443d98-0dbe-32cc-83db-4c1ea4cd5c7a | -12.66426 | -53.19187 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7beb4017-9d45-3c11-aff1-21a70eebff61 | -12.66371 | -53.19545 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42f42b89-fa45-373f-bdc8-158d39ae5a14 | -12.66092 | -53.19134 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01afcdcd-200b-3a97-8f48-a86f3682a5dd | -12.65757 | -53.1908 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dec91351-eb05-305a-b947-34e78c22a3c1 | -12.65423 | -53.19028 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c689ccbe-5d99-3dc2-9157-faed46032c26 | -12.64699 | -53.19278 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c01a1dc9-6d83-3f93-87f5-761e5bea3a69 | -12.64365 | -53.19225 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c4b6d86-96c1-37e1-bb0f-41c92710c272 | -12.64085 | -53.18814 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f2268aa-049d-3b6a-a360-fdc0e7cc455f | -12.62266 | -53.28407 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eca21cff-bf39-37d9-958c-91a8883175c0 | -12.62198 | -53.18858 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbae8cbf-78ab-3640-897e-48e5155a63c2 | -12.61359 | -53.15422 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c04d66e8-2c42-390f-a2d6-df40e8f1dcbd | -12.61304 | -53.15781 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa020efa-152d-3ae6-af97-33340b2ccc28 | -12.61074 | -53.49373 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e241c28-23f1-378e-8aad-518a9d6bf621 | -12.61025 | -53.15369 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36d92809-b74a-30e5-8732-d1fc5711293c | -12.61018 | -53.49728 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 905c19ef-17aa-33d4-95f7-349c73675e79 | -12.6074 | -53.49319 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd4a29e6-ef0f-3705-83d2-3b0f83351d5a | -12.6069 | -53.15315 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5865ad23-50ac-3de8-ab83-55647c9de9e5 | -12.60685 | -53.49673 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d414c307-fb12-3a09-9274-2652ffc5f2b2 | -12.60407 | -53.49265 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65996c19-450c-3ac5-9d87-69d9d1e19a43 | -12.60356 | -53.15261 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1596fcbe-8b3b-3fec-9ce3-784d8fa0280b | -12.58849 | -53.13919 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eddb89ea-b14d-3a51-9b14-5edb7d8e78ca | -12.58514 | -53.13865 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f97f5cb-da3e-3e3a-a032-8dd18ba8d39d | -12.5818 | -53.13812 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 790ba11b-e2b5-33c0-9191-ff1a72931eff | -12.57252 | -53.28679 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| badebd75-b074-3685-935f-f79a8b4d82cf | -12.57176 | -53.13651 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9efbbec9-8139-39d8-8e45-e9a7ca62d9a9 | -12.56897 | -53.13237 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2b2b3b7b-8d48-3a24-8a0c-d4ff4727ea67 | -12.56841 | -53.13596 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 882f5875-3400-3f22-b464-5599ce3918c7 | -12.56562 | -53.13184 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0b95cf3e-e631-35dd-80ba-93e3243ef350 | -12.56529 | -53.28928 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cafb396-e130-340d-8604-8abbab32dc0b | -12.56507 | -53.13542 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 81585aeb-47f9-3499-b2b4-a55e8a7af260 | -12.56452 | -53.13901 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 582ad551-4998-3a31-8e30-ae11cf046f2f | -12.56195 | -53.28874 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35c67abf-1b93-3040-a94e-745cd74e5e8c | -12.56172 | -53.13488 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc6e4e13-743f-363c-b04b-9180bfe76269 | -12.56117 | -53.13848 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2f87d0e8-bb65-3aae-91ff-a727e5a3d73f | -12.55838 | -53.13435 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c41c46d1-f74f-3e99-914b-4d6d62970688 | -12.55783 | -53.13794 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 696e5f1a-d870-373a-90d5-d6e1163934eb | -12.55547 | -53.48457 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09018ca3-8b40-3186-860b-bf1dd600b2e0 | -12.55448 | -53.1374 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c8a36ac-6dbb-387d-8eef-4079d40c06a4 | -12.55393 | -53.14099 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6dc3733c-dcba-33d5-ae2d-397dba6efc35 | -12.55269 | -53.48048 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa0e1789-87e6-36bb-84de-e27450962437 | -12.55114 | -53.13686 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 702e28ed-42ae-3df4-9c5e-06b7e1611829 | -12.55058 | -53.14045 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67a1ba90-6b15-39ab-b42a-1f0066f13625 | -12.54936 | -53.47994 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b36bb53d-d286-3183-8fe3-2ef62f84ad49 | -12.54724 | -53.13992 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f24221e1-cdf8-3e6e-b343-3917be148f3a | -12.54658 | -53.47586 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a609190-028c-3fec-883f-36be60b9b511 | -12.54581 | -53.2825 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b8d3d33-7317-39d4-b2d1-7e0775b5c4a6 | -12.54444 | -53.1358 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88c8454a-9e49-3fbd-bfa2-883fc8ac73c1 | -12.54389 | -53.13939 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97137b0f-9580-3ade-95ad-7c73f0567447 | -12.54325 | -53.47532 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f1e21f7-4a87-39d5-82cf-1a2555b45ebc | -12.54302 | -53.2784 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d364f07-bff1-37fd-b3a8-e0252f08a1b2 | -12.5416 | -53.10963 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b5aae25a-961d-3553-8112-cbf117423301 | -12.5411 | -53.13527 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 308204b7-46bd-36f8-93c3-d74e6a528ab1 | -12.54105 | -53.11321 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eb7a131d-45c5-31fc-b4be-2cdd66dead84 | -12.53968 | -53.27786 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc86aca2-7075-3996-8b50-de80bc4021ce | -12.53957 | -53.10956 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5136a063-8ba6-3b46-9307-5627824fa638 | -12.53902 | -53.11313 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 576ec7ff-66c1-39e9-905f-eff6c28902fd | -12.53847 | -53.11672 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c383e191-227b-3be5-99e6-18e652e9f252 | -12.53658 | -53.47424 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5d34799-903e-3773-a154-8dd6866dfec4 | -12.53623 | -53.10903 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61137379-0ceb-3930-8576-9aa86eb5d209 | -12.53512 | -53.11618 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80550553-0cd2-31e7-a82b-c1427b1dab03 | -12.53456 | -53.11976 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3ceb9cc-0ecd-301f-b0ab-9670f8ff8f5b | -12.53411 | -53.26966 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea3d21ae-2545-388e-90fa-6993ecb178bf | -12.53407 | -53.24771 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e4f2fa2-1f05-3131-a41c-9b991afd6c31 | -12.5338 | -53.47015 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48cce42b-dc20-30b0-886c-de98ab963185 | -12.53352 | -53.25129 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e12b8dc-86bc-38e7-a57a-cade5651f29b | -12.53288 | -53.10849 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d54c381c-bedf-3c3d-b318-d1bdcc135efc | -12.53242 | -53.25843 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f0d57b0-5854-3dc1-b254-3f9114c046c3 | -12.53233 | -53.11207 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5478148e-f6e8-3baf-893b-32aa9029634d | -12.53177 | -53.11565 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8783ca8d-a191-33e6-ac3c-a5abfbcd7566 | -12.53132 | -53.26556 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 449423fd-13b9-382f-93c3-513a2109415a | -12.53018 | -53.25075 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README132.md)
