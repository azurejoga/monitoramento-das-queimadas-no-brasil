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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fe70f23-09dc-375f-aa91-b73cd200e925 | -6.54599 | -56.54244 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 665c1dda-07a1-3b39-9fa9-f89c86b6fae6 | -6.39562 | -45.68987 | 2026-08-16 05:16:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c47df6b-d2fd-3b3b-8340-3cc830996af2 | -6.96961 | -59.29911 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25da78f4-8d88-353d-b2b8-db674edcae2b | -12.00543 | -46.42849 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 57ca34c7-44fb-305b-9c56-091c72002d54 | -6.21438 | -47.73116 | 2026-08-16 05:16:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| ec0ed033-6295-3bb5-ab2a-03d3f9f778f8 | -12.02194 | -46.44114 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| cee26734-558f-3239-9682-428fb7c34ca5 | -6.82538 | -56.44816 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4cd0edcd-b974-364d-882b-2de72bd4c816 | -6.73381 | -58.5867 | 2026-08-16 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d0d3f1a-2949-34cc-88f2-7a0859dea14e | -3.59894 | -56.80836 | 2026-08-16 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 510e6d2d-8046-3959-8474-41e5cae9b1ad | -7.41146 | -60.01096 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e7a9947-bdb7-3949-a90f-c7f474860a93 | -6.11787 | -57.70373 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d3d2e93-5f13-39e0-b47a-4a68c07f923c | -6.11661 | -57.70671 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8a16a042-2554-3223-ae19-80b31e5eb7be | -6.8287 | -56.44868 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ca09fd5e-f0ab-3dcf-bb1c-77673689b20e | -12.23958 | -47.01283 | 2026-08-16 05:16:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c11c2b07-77a0-3490-b845-11d2d61ed6d1 | -6.96527 | -59.30274 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3be9a29f-d994-32f1-bc76-185cb5d940c1 | -6.79226 | -43.0312 | 2026-08-16 05:16:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18861c41-6e60-366f-877f-7b995898204a | -6.84722 | -58.97488 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f8fbd361-8819-3974-b809-4d56aabeef03 | -6.81374 | -56.45702 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec643db9-27b3-3666-9ee5-fc83f5a2d3c3 | -8.96002 | -60.53044 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 21eed79a-7b60-3d50-8851-90ddaf23b1c0 | -12.02808 | -46.44014 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e8e21b28-5579-3d32-833d-04e83e76926c | -8.60887 | -54.69886 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b684231-957b-39a7-a129-92077a3ed45d | -10.52315 | -49.45509 | 2026-08-16 05:16:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6c3c07c-7412-3d0a-b8f2-b9b625e8a685 | -11.50694 | -54.62151 | 2026-08-16 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cb85ec8-d870-3f79-b3a0-d82ceb001fe8 | -11.91174 | -50.23649 | 2026-08-16 05:16:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df47956e-dec8-3717-82a6-d6f2f83f1ed3 | -6.6035 | -58.98298 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1112dc2a-73df-3cf3-a967-81e00963d1e8 | -6.8442 | -56.43689 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5dc2dc53-18bb-321b-8de7-d81c805f5a31 | -3.51112 | -58.95196 | 2026-08-16 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c199bc08-94e9-3120-8297-49c92a67adf6 | -11.08255 | -47.24877 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5250c89a-a6b5-3086-8780-6ca518dbe67d | -6.95508 | -59.2967 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6319951-3b4b-327d-a2b5-bf746aedee4a | -6.95871 | -59.29729 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37d4fbe2-3548-3413-8aff-6f9ef9914cd9 | -9.09702 | -46.39353 | 2026-08-16 05:16:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f22d22ae-dc0f-34a7-92a1-23c21c154175 | -7.0665 | -56.65431 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b602ada3-0353-3b1e-8682-b940fc43e154 | -8.98129 | -60.51973 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7915b4fe-d62d-39c2-b5cb-c5dff6363d97 | -8.43651 | -62.68854 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9e5b5e71-6889-3149-8ffe-c9ad674d7629 | -6.10925 | -57.7137 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 3826481d-52db-3daa-a130-073d1b08e698 | -6.09719 | -57.72317 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1895be8e-55c9-32a6-8ba3-06aa1d4eb423 | -11.88392 | -50.61745 | 2026-08-16 05:16:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c83d3d6f-4e22-3782-b29e-7d27a088bc84 | -6.85147 | -58.97138 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dbd5afbb-b3d5-3925-810c-5b1a2f3c3bc6 | -6.61782 | -59.05328 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5fec873-100d-3641-8255-e0641139b567 | -7.06706 | -56.65082 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4deb7d86-d8f8-3dfb-a048-999176ca740c | -8.97528 | -60.5092 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 77e55da3-28b5-3650-95b8-d309e0210f33 | -8.95858 | -60.51588 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e808c18e-d7d0-33f7-b536-ae21a573f298 | -8.9745 | -60.51384 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0c992d06-a4d8-38b6-8994-d3a8288469e0 | -7.58381 | -60.89024 | 2026-08-16 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6077c4ae-d095-358e-b3dd-4eefd51d701d | -6.21939 | -47.73187 | 2026-08-16 05:16:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| d5468320-a1db-345f-9fe2-9db30d73cadc | -11.62255 | -51.09105 | 2026-08-16 05:16:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3476e69-363b-3fdf-85cb-4f08c2b6997c | -8.90226 | -60.55618 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a7ada8b4-fbb2-318f-9f1c-7d71b626db54 | -6.6223 | -59.07114 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| be139b87-266a-3f6b-8eff-351417b096fa | -6.61713 | -59.05746 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19997e53-6a46-3e8f-87e2-b3ffb23509f6 | -8.65056 | -54.72381 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7197fbeb-e334-35ce-925e-abfa42e7c8af | -11.80908 | -51.78916 | 2026-08-16 05:16:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2ba83c6-2461-3f0c-a080-5f91d3a6beb2 | -8.61229 | -54.6767 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71f9e5f9-9dde-347e-b44a-e0d8f9edd56f | -6.81098 | -56.45301 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ec7f142-e695-30fe-99e9-ad59740d2681 | -8.89466 | -60.55489 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f40a8da3-cb8d-3063-9be2-d4545190827c | -11.20614 | -54.82085 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00460838-b697-3189-8147-4424c0483864 | -8.34917 | -45.98265 | 2026-08-16 05:16:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76f45900-4919-3ebf-997e-c301285d3d3d | -11.06538 | -47.26223 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45cc12ed-18db-310c-a5cf-ff7a5b339ad8 | -6.61428 | -58.98471 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d15af82-6ef8-3b5f-aac7-7173dbc25162 | -11.47939 | -46.59261 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| de10c2bf-49e6-3923-ae8f-b1789e89b6d4 | -6.62162 | -59.0753 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6cad1d86-1c95-3212-a1f4-19091b00ba85 | -6.86302 | -56.42566 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0df9581b-d03f-3341-bd45-e42ad21ec49a | -11.10552 | -47.24567 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1cd46481-c892-37e3-a641-f9d215963bd5 | -6.713 | -58.93253 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 330ef15b-5c24-34a1-9d79-5b7c0d3e9651 | -6.84918 | -56.427 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fa6c499-dd15-381e-80a9-8f0960cad527 | -6.30723 | -43.61742 | 2026-08-16 05:16:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 7dddeab4-e13a-3516-9f22-013ed73f8fb1 | -6.8597 | -56.42512 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48099be3-6dbd-3384-b436-39ae6337c793 | -6.59718 | -58.99888 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d2a50dd-289a-312c-bdfe-a7940e1d7675 | -12.02754 | -46.4446 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 49be5a7b-3b5b-3edb-a069-e22a376f5665 | -7.55565 | -61.17734 | 2026-08-16 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9e1f8a3f-e7f9-385c-9444-2547d260cb62 | -6.81485 | -56.45006 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e88a3980-dccb-37ae-8021-15b4d627eaef | -6.09436 | -57.71891 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70052688-be0e-34c4-8dc3-e3f29296611b | -6.63692 | -56.39981 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89a74063-6af3-3a5a-b5a1-e3857b84057d | -8.61285 | -54.69571 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6fbb252d-a3d7-3568-acea-126b6a29561b | -8.95357 | -60.59173 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 936936ea-eebe-32a6-a7a3-f55a20f745e2 | -6.70518 | -58.93536 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 509803ee-2405-3280-8a5a-be32b7d8d7f4 | -11.05524 | -47.25332 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 069714b0-40c3-349a-8878-29ae8c9968b5 | -6.59135 | -58.98947 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4d9b090-cf90-3e8a-a381-d1c53eb75136 | -6.3138 | -43.61829 | 2026-08-16 05:16:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| d977b0aa-e092-354a-98ad-6a447ce67071 | -9.47744 | -60.53765 | 2026-08-16 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b88b0291-3c6d-353f-8c79-9ea98acd510f | -8.99027 | -60.60042 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adc145ee-ed37-3a0d-9e66-daa96b88d435 | -6.8711 | -58.94112 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c1b963b-f63d-3bfe-8f4b-7f9b4173f850 | -8.90194 | -60.57331 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bdfbe377-5888-3be7-8f2b-a3f14a6b11d9 | -10.5355 | -44.85008 | 2026-08-16 05:16:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e365607b-6b91-336d-b7a1-75beb8756ac0 | -8.95072 | -60.56231 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 635ebb2f-f0c1-3ec0-afbf-7bd5fd382b6a | -6.85195 | -56.431 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e073b527-6b10-3e9a-a112-5a203515937a | -9.47461 | -60.50893 | 2026-08-16 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 432dd4d9-8afe-3fc7-9ee4-2e9c7278c1c1 | -6.11882 | -57.71465 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ce7a92b-ad52-3251-84e4-d76408ed4a88 | -6.84586 | -56.42647 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc735906-5afa-396b-8a68-95a88d0ea48c | -6.60149 | -56.36564 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07cd7d29-cb66-3d5c-a92d-74ae40f489ca | -6.22 | -47.72662 | 2026-08-16 05:16:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8aeaeb44-0f57-38ea-af0c-14c85d221c29 | -6.86247 | -56.42913 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 265c09c4-f1a3-33a2-b0fe-ef2c93f7237b | -6.7159 | -58.93721 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ab177abe-dfe8-3e89-9fe7-a370d6a3f8de | -8.6083 | -54.70255 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9eec71b3-ddb5-3995-aa41-5c3994a10299 | -8.97438 | -60.53769 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c91ba64f-e457-34e3-84b7-140b5f555566 | -6.88607 | -59.01799 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ee1cb64-0e8c-3291-a777-527166440f80 | -11.7113 | -49.07673 | 2026-08-16 05:16:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b4a40e5-f20d-32e1-af0a-225c57efa9e2 | -6.96598 | -59.29849 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a39c9e2a-87c3-32c8-8973-2f1ef513113e | -10.52243 | -44.85401 | 2026-08-16 05:16:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad82117f-6b73-3339-9df5-19a17ca3b87f | -9.35039 | -62.36869 | 2026-08-16 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b3779497-7b80-3852-978d-147c27b116e5 | -11.89361 | -45.96312 | 2026-08-16 05:16:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README42.md)
