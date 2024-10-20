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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ee12f8c-be11-3fb6-8795-48a34395d0de | -3.82926 | -48.884 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d45b80cc-ccc5-3573-af6d-b83fc90eebbd | -3.82136 | -48.86772 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1824f618-66c2-3be4-a94d-f1d2f8e334c0 | -3.82077 | -48.87138 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0521e3a3-04ef-3fd6-bdd1-e367d164b830 | -3.82019 | -48.87504 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8e0f0bbd-5db4-3d2d-9178-baadc200df16 | -3.81795 | -48.86718 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 77472a69-734e-3d8b-b19c-283c24806052 | -3.81736 | -48.87084 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2e714fed-3130-3edf-a474-12bf4c33e4aa | -3.81678 | -48.8745 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0b7dec8d-2e9e-3f06-9b37-c611f1c392e4 | -3.81395 | -48.8703 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d17a6cba-79ec-3591-9839-c1319fd34efe | -3.81337 | -48.87396 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e8897128-bff4-30d5-9f01-361fac1d771e | -3.76147 | -48.89203 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 50045515-f63f-32b5-88d0-3aee7f3a3080 | -3.75855 | -48.89154 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61daaba0-f6af-349b-b75c-2df2af5c3456 | -4.1865 | -48.03934 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46b45efc-3e30-3ecc-87f9-00c35447170d | -4.13417 | -48.28323 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c497b5f3-6060-3387-86b4-78ff31a2da68 | -4.13138 | -48.27916 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c28d9052-1142-32b8-b213-47663d19122d | -4.13082 | -48.28268 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24bb3fec-c570-3ca8-8c9b-18594872f7ac | -4.12243 | -48.27055 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d221a73-ee99-3f91-be15-9a81bb7efd6e | -4.10346 | -48.2386 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bac9399d-eda7-344d-bd5f-baf91037f487 | -4.1029 | -48.24212 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 07b60c11-e995-3beb-8415-4cdf1f4a59f7 | -4.10011 | -48.23809 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 58e9e457-6392-36e3-9804-73d88f61e23d | -4.09955 | -48.2416 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9b179e5b-8480-337f-a8a8-998f47a081bb | -4.07938 | -48.28184 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4b73d3b-caa1-3080-8f39-1bb8da1201f9 | -4.0729 | -48.24848 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 366c2648-c837-3ea3-af60-4e7f23827e25 | -3.96401 | -47.94739 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1e67c41-d52f-3b99-8229-561bd804c5a4 | -3.96012 | -47.95036 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 634a2326-fd1c-399f-a36e-e858da4b9beb | -3.92956 | -48.36041 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0bd59dbc-2004-3900-b37c-3081a4266372 | -3.9262 | -48.35988 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 064853aa-2b2c-36b1-97ba-847e4dd71d8a | -3.92341 | -48.33393 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63254d5f-8050-3e6d-ab2e-0214c5d4ff4a | -3.91781 | -48.32581 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ce10c39-5046-3cfb-b11d-747e667492af | -3.91778 | -48.3695 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9a5eaca3-b0c7-3710-b884-da087230f02c | -3.91277 | -48.33588 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ccc0d343-a9ad-3dd2-b44b-893047a5143f | -3.9122 | -48.33942 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b1a76167-7598-3408-89cb-05a108268748 | -3.91118 | -47.95695 | 2024-10-20 04:32:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cf70c8b-bc44-38e4-bb84-65d5de22b2ba | -3.90884 | -48.33889 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 428bc794-7da0-355a-bd95-b09c53fd2f95 | -3.9084 | -47.95292 | 2024-10-20 04:32:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 797a80e6-2faa-371a-998b-7ad478d5cc26 | -3.90826 | -48.36434 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da4bbeb8-7504-3fdd-94cd-f6e9fbfb7a5d | -3.90784 | -47.95642 | 2024-10-20 04:32:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82662030-c0d5-3b84-8e6f-5a0113507e8e | -3.90548 | -48.33836 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18b22ad3-cbd0-3429-9aae-4f0693b290bf | -3.89988 | -48.33025 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54ecf68a-9a32-3665-9308-f59b8fd0bc7e | -3.8976 | -48.3663 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bdf9276-0fb1-38cd-a13b-c6b1925b61a1 | -5.33885 | -48.35017 | 2024-10-20 04:32:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8e3e1e0-65c7-3d36-abdd-b32184b58cd3 | -5.33829 | -48.35368 | 2024-10-20 04:32:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 039bcfd7-4a8d-3f2c-8dab-3de58858bfe1 | -6.23378 | -49.07407 | 2024-10-20 04:32:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57c7405a-1460-3999-87e3-4bd9301cee6f | -5.30569 | -49.49999 | 2024-10-20 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c809ea6-ba36-3359-8169-33b22d82f942 | -7.07928 | -49.14183 | 2024-10-20 04:32:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 006a3765-1b85-3d79-80ac-c93b3d32f861 | -6.99131 | -49.42373 | 2024-10-20 04:32:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c042b9b1-5afc-3919-85d0-7ae6ba050371 | -8.31785 | -49.38324 | 2024-10-20 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3afe092f-4aa8-37b8-a765-ace416e371bf | -3.55 | -50.30905 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f448fbcb-4a90-37ff-a920-d88375162fa2 | -3.54932 | -50.31322 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0d668d5d-3aa3-39c2-bec6-30543dd4732f | -3.54636 | -50.30847 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 09bc44c0-7a54-38c5-84e9-fb9d892764f1 | -3.54569 | -50.31263 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e361ea7c-0e15-37e2-b893-b5440be7ffcd | -3.4751 | -50.35859 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c93075e1-bc6b-30ab-81e6-f1b2c922acaf | -3.47145 | -50.35796 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a749989-7459-35fc-9d62-6d36440fc0d5 | -3.46985 | -50.34467 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10c35351-97fe-365d-94cf-2a4a0d9a6fe3 | -3.46781 | -50.35737 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5af49bb-88a2-3138-9b16-2b63f8b2819d | -3.45628 | -50.17553 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| faf1a85a-4c61-3685-89f4-0d62522c812c | -3.45367 | -50.32914 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc7f625d-2fda-3ec6-bec2-b5b11520ba40 | -3.45003 | -50.32858 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6308e23-13c1-33e0-98a9-66b3971a853c | -3.44182 | -50.17326 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77937d0e-d01a-3bdc-8518-be081aa29334 | -3.44116 | -50.17734 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 954373b9-60a5-37ad-a731-c4ed0640128d | -3.44073 | -50.17443 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49738ad6-254d-3474-a7b4-7cf0c99b4b1f | -3.43846 | -50.19382 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a3f979e-aeb6-347f-b9b9-3570172901a3 | -3.43747 | -50.19505 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b178e6e5-40d1-3c5f-8fe9-e6a4d4015045 | -3.43418 | -50.21587 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e23621ad-e9a8-33d6-8aac-b4d940b3927f | -3.43182 | -50.32571 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 684838e6-b8f0-3bb7-8984-f12d30760be8 | -3.43123 | -50.21108 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aeb8b213-8481-35db-a006-1b0b4c396220 | -3.43057 | -50.21526 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01343408-cf4b-39d3-ad2e-832cab1735d8 | -3.42761 | -50.2105 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5334598-5c8a-309e-8404-3b91aabbea2c | -3.42695 | -50.21468 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2562fecc-0fbf-37e8-abaa-6e194fce67ea | -3.42398 | -50.20995 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ad9dcf5-aa92-3c16-a8b4-805f0958d26d | -3.41852 | -50.38429 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99c9e0a5-f48b-32ef-bd7c-f9f4ce0a5c1c | -3.38745 | -50.34608 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4b3b5fac-7188-32b6-9de6-60ded47ec125 | -3.3838 | -50.34551 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 38e81bac-8807-39b3-a781-b5b6e4bca09f | -3.38015 | -50.34494 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 17fd52e0-9915-3467-8beb-29fe6327f9b5 | -3.36505 | -50.29926 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d07c2973-eb6b-32bc-9400-d360974922f8 | -3.36073 | -50.30291 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d1ca7e8-59c4-3235-84e3-6ff4a50541a0 | -3.35708 | -50.30235 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d180d4f-5e26-33b4-80d6-6430cd68d13d | -3.50162 | -50.53659 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f0af816-1d00-3e54-a36f-265ee2fc8536 | -3.48031 | -50.49042 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf03e519-7206-3ef3-9e99-640bfad63431 | -3.47663 | -50.48986 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5d439b91-2cbd-3d30-9a27-cd21c4e55c26 | -3.47595 | -50.49413 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9db392e0-c1fa-3c78-8e93-b1b76cef179b | -3.41618 | -50.63097 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7901b530-8796-3121-bf6a-e7c8c46c0a0d | -4.98118 | -49.76097 | 2024-10-20 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4afa7dd7-1502-3558-b280-730ec051c57b | -4.97845 | -49.86759 | 2024-10-20 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ec77384-49e0-3f32-bf69-32d677edb89a | -4.96877 | -49.59451 | 2024-10-20 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a3dd67c-a5f3-3120-82ca-616966180ae3 | -4.88225 | -49.92925 | 2024-10-20 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90f5db50-243c-310e-9247-bb6b1c1b7b48 | -4.88148 | -49.75386 | 2024-10-20 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e538aeb-88c6-3d86-a3ee-382ab2aa436e | -4.84067 | -49.91856 | 2024-10-20 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3567e1a3-c42f-3960-b8de-804c8d03b374 | -4.83083 | -49.95719 | 2024-10-20 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d121c70-d1c4-3555-9617-70a7333fd904 | -4.82731 | -49.95661 | 2024-10-20 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46eba3f4-43b2-3beb-8e2f-00482ad8b744 | -4.80994 | -50.59311 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04c0f6f3-02e5-383f-b585-ce638c14080c | -4.80925 | -50.59734 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 229ab7dc-6b02-355d-943e-0e1922c35dd6 | -4.80644 | -49.58929 | 2024-10-20 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 306ad64a-70e2-3e47-acaf-d2e1d9645df8 | -4.80632 | -50.59248 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29d7ef26-f77c-341a-bf18-5c9340c5e1be | -4.71179 | -50.73996 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ad1935e-c496-3406-acdd-2ba60657cb35 | -4.59152 | -50.67382 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54071c64-a4d3-346f-b236-50de0e2381e7 | -4.58786 | -50.67325 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1c24afa-5647-37fa-bbe5-03a7f2e8eb9f | -4.58716 | -50.67751 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ad0d258-884e-32c7-a522-681bc261ea22 | -3.69194 | -50.19406 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 81ac6c6c-91f3-3930-a9e7-aedb7e693ac6 | -3.68833 | -50.19349 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 028e3910-3625-3953-b613-f03df7c7fc9d | -3.67768 | -49.79065 | 2024-10-20 04:32:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README37.md)
