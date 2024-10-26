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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e4d9230-a329-3078-9ab6-e002ec4fd1ad | -4.33161 | -48.63815 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fadb815c-c7ad-3f96-8673-dcf01dafb9d8 | -4.30255 | -48.64367 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 959f0edf-6f3f-329b-b1bb-bdb2913653f5 | -4.30173 | -48.64866 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5b8cf09e-ec74-3551-bcbe-d2ee321bdcbf | -4.30091 | -48.65367 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a1bfa37f-d531-3135-886d-30f916164000 | -4.29782 | -48.64797 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 32be058c-a5cd-3e80-b58b-00be00daa7cf | -4.297 | -48.653 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0f8e85c6-aaae-3d98-a2fe-7cc2e9bdaaf5 | -4.28832 | -48.65675 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88f06edb-75c9-37b5-acc5-a75ce1078858 | -4.27563 | -48.56377 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65ae04da-7a2b-34c1-bf5d-af81e1616e0f | -4.27499 | -48.56662 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c09915d3-2ea7-30b8-9e26-7a335084f0f1 | -4.25009 | -48.5472 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65c19327-6396-3ed3-b996-0a3fb0bb95e2 | -4.2493 | -48.5521 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 97a9c809-b8e4-3f6d-8149-8e2df766a956 | -4.24618 | -48.54661 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 27010ec2-0793-3d5e-a39f-5571c2a8d46d | -4.24228 | -48.54601 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e13f1be6-13c1-31bb-9ef9-f0de5c930be3 | -4.24149 | -48.55086 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f693c652-8499-3022-8f15-e4aeef7a52f1 | -4.2407 | -48.55572 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7635b21-6cef-3580-9c19-1152e96a6f24 | -4.2368 | -48.55508 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 963c83a6-8f1c-3d9c-abe7-0210b2666839 | -4.23601 | -48.55996 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f7830a1-d8b1-3e44-a23b-3d8d057e42a2 | -4.2196 | -48.56234 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f8775f4-ba1e-33b6-bb68-47c5fdf17c96 | -4.20877 | -48.03779 | 2024-10-26 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31c83c25-0566-3821-84ea-1b7aa2ee9129 | -4.20349 | -48.04642 | 2024-10-26 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 30f7b2a1-c74f-356d-b153-eb8f58181273 | -4.20047 | -48.04111 | 2024-10-26 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 99ffd78b-cf5b-369c-b4a0-ffff39c74af2 | -4.19276 | -47.99318 | 2024-10-26 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6eceff8e-99bc-3193-baf4-1d57cfdb48c6 | -4.17016 | -48.5982 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f15a1d79-4a66-39d8-abd4-c46ae240d6a4 | -4.16927 | -48.59981 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 43e71ae9-f966-3335-95a5-14d524a5fb97 | -4.11782 | -47.95446 | 2024-10-26 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bec01604-017e-3e6c-9525-50142139fea3 | -4.09978 | -48.23654 | 2024-10-26 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e732ef0a-6a54-34c0-b69c-97e069f128c9 | -4.09698 | -48.50538 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87e36ad9-0061-34af-b394-5f7aa6919cb6 | -4.09593 | -48.236 | 2024-10-26 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cf1d9729-ce9f-3c08-94ff-8cffd2b89c1a | -4.07142 | -48.24159 | 2024-10-26 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e9f1b3f-25b1-30fd-bb6b-d677d5c2ef63 | -4.07069 | -48.29496 | 2024-10-26 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8511986-fed3-33b5-a050-035cc3b2d384 | -4.06683 | -48.29441 | 2024-10-26 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e47a272-3d7a-3d12-8c5b-2cb27c9965ca | -4.04848 | -48.11758 | 2024-10-26 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd3e3403-6a8f-3a40-9a27-5731c4fe561b | -3.93644 | -48.36018 | 2024-10-26 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15675447-9797-3d98-bc44-18a0cfae8772 | -3.93185 | -48.33949 | 2024-10-26 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f317ac9f-5fdc-36a5-a236-a602e7542e52 | -3.93107 | -48.34428 | 2024-10-26 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 76f1dbcf-537d-3b1d-b3bb-18085c345cf3 | -3.92799 | -48.33884 | 2024-10-26 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7fc3aab7-b1ec-3747-999f-3c29b6ec8873 | -3.9272 | -48.34367 | 2024-10-26 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| fc44136a-7850-3e66-b366-ca346128a60c | -3.92306 | -47.96564 | 2024-10-26 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99579d6b-bd8a-3438-88c9-4ca4a568402d | -3.91094 | -47.94445 | 2024-10-26 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b4ffc3f2-292a-33b7-a01b-d5207dd9dd3a | -3.91083 | -48.37096 | 2024-10-26 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52fafbb5-b4c1-3251-b003-57c230f7a630 | -3.90946 | -47.9537 | 2024-10-26 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbcac99e-8b77-3af1-a7fb-f3bc5278e9e0 | -3.90695 | -48.3703 | 2024-10-26 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 817d1a8e-b64f-329a-9ccb-f05d4eb0b88d | -3.90643 | -47.94842 | 2024-10-26 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d50163fe-38c2-362a-bff8-672dfc082c6d | -3.827 | -48.88186 | 2024-10-26 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ba10aad-ba53-36f8-b36f-1d1ba7e123ce | -5.21763 | -48.22311 | 2024-10-26 04:17:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dec8dc0d-a1ef-3bfa-af97-fa552cd4b3a7 | -5.21386 | -48.22249 | 2024-10-26 04:17:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 903b236c-4405-3b80-8bd2-1c8fc609dfdf | -5.21009 | -48.22187 | 2024-10-26 04:17:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b2feb646-22af-3ee2-a9d1-2f76ecbd1e40 | -2.17926 | -48.84248 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e1786ef-46c3-3fc3-bab2-2e4d3454f99c | -2.18477 | -48.8441 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4cf9bd8-e7a7-35be-b57f-9cc06ed36a8f | -2.18335 | -48.84313 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1235a2b9-9415-3ef6-9150-108a9dfbc37e | -2.18067 | -48.84343 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96360705-8053-3589-8977-7286bcf048b7 | -2.69179 | -49.04746 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1dc8ac3-c2e0-3bfb-9e9e-a28fc1269e48 | -2.66084 | -49.27622 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03ba3eb7-fcc8-345b-9fee-e1f9087b8e91 | -2.66021 | -49.28004 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94dab5ae-eb73-3138-8a72-4ddfbb9fcbfb | -2.65716 | -49.51027 | 2024-10-26 04:17:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7dac21eb-5a26-3fea-82e3-4856eab5e21b | -2.65666 | -49.27554 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23c39e08-a913-382d-8e8e-ec732f44f025 | -2.65639 | -49.27221 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cf12a0d-e675-3115-94cb-643c26013d92 | -2.65602 | -49.27937 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f885bc1b-4ecb-3a43-a501-9c2d8875681c | -2.65579 | -49.27602 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7dd4129-36a7-3bd4-9350-5029e9eaf73f | -2.65291 | -49.50959 | 2024-10-26 04:17:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cdc655f7-4cac-3a26-bea0-827118ef98a2 | -2.63552 | -49.24153 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6245d60-c1b0-3772-94e1-028afeadcfd4 | -2.63491 | -49.24532 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00851af7-2880-3f1d-8e9b-f2a97b5bb5a8 | -2.6331 | -49.25671 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0d3289b-922b-3509-8e36-f8aa2294acf3 | -2.63249 | -49.26051 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 847840d3-c112-353e-b384-f7a48bd74ba1 | -2.63013 | -49.24845 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96b2c5f8-4343-3952-9df8-c80ef52118bf | -2.60323 | -49.09767 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e2fc01c-4282-3e65-8bac-ad8c78e72972 | -2.59909 | -49.097 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 558ce7cd-efd4-34b4-96c1-f2b0a80f6811 | -2.59847 | -49.10075 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 462e1771-f6db-3383-a74a-e509966e5f04 | -2.58894 | -49.23784 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a21be7d2-7965-399f-b98d-8ad9212ccede | -2.58538 | -49.23338 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4a2c943-7591-35af-a5cb-e8882038741c | -2.58477 | -49.23716 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 36a75284-2472-3d35-a1b4-6b2815cc15b1 | -2.58319 | -49.19428 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b1f7b1f-0e2c-350a-9513-120434e59854 | -2.57517 | -49.2434 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd0280f5-1dcf-336f-9345-232ef5adde31 | -2.57284 | -49.23137 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6108bbec-3fba-3550-9993-bd61540a7213 | -2.57223 | -49.23514 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e996f9b7-66aa-3578-b502-1cfd080f5e8c | -2.56866 | -49.2307 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 33ebdd39-9588-3bcc-a25c-160ab88e7d7d | -2.56804 | -49.23448 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dda3ddae-85e6-35e6-bba8-f2e7398a3448 | -2.54015 | -49.81185 | 2024-10-26 04:17:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 876f9921-6d6d-3e05-b902-be884fcb7db0 | -2.47328 | -49.10335 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1c04e8cc-6a6b-3397-a47e-f7d741e2903a | -2.47266 | -49.10709 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 67f07c6f-9ece-3111-8cf2-966e6959cad1 | -2.46912 | -49.1027 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0d1fa743-45e4-303f-ab69-f1083fdcd894 | -2.46851 | -49.10643 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 47fa433d-52bf-3d26-8bf0-29f21e272945 | -2.46743 | -49.10294 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 10a6c8f7-4594-3932-9757-9e1cf9336930 | -2.46685 | -49.10668 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9eff35f4-0ca2-30f4-96dd-37a8f35a8cf6 | -2.46436 | -49.10577 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12f48113-d13a-39dd-9ecc-dd52962f499a | -2.46377 | -49.01851 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aaa9e5f1-f1c0-3844-97d7-f8e3da6457cf | -2.38849 | -49.38425 | 2024-10-26 04:17:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c49ba8d9-67a8-3c96-8074-1ba9d04699f0 | -2.38787 | -49.38814 | 2024-10-26 04:17:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffa67659-7cff-3eb2-a372-c0616d00f21f | -2.38425 | -49.38358 | 2024-10-26 04:17:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9b64653-7cb8-34db-9c79-139946d2fc0e | -2.36914 | -48.93618 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8e20e1e5-9add-337a-99fb-ab5b84bc97cf | -2.36855 | -48.93986 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e914597f-e8a2-3c42-9b7f-1d82ecbca3fb | -2.36091 | -48.93489 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 804771cb-2942-3aa1-8c33-17403d2d38ac | -2.3568 | -48.93423 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b88f1bb-55e6-381c-a332-b0ff64b20c0d | -2.28873 | -49.52793 | 2024-10-26 04:17:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f83f568-4a71-3aad-908f-7796a0bc3b86 | -2.44998 | -50.37574 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c304b71-f941-374e-87f4-356a07f6eb13 | -2.44546 | -50.37499 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a455db21-a161-3435-a3f4-058871612582 | -2.43975 | -50.2953 | 2024-10-26 04:17:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a0a7a53-e151-34f4-a1ed-ed4e4478ad31 | -3.15776 | -50.46221 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e4924ef-1fe9-34b9-9a4b-3c13dcc901ab | -3.15326 | -50.46147 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cc5a6e9-f31f-3b90-8726-328735adc4c1 | -3.15252 | -50.46595 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README43.md)
