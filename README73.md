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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b53bf9a-9c3e-3af3-afc9-4406013bf48f | -4.29291 | -48.60909 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 94b554f4-a5da-3afa-9a0f-3e20e85641ec | -4.29226 | -48.61359 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 087b4a2f-d14e-3c0f-a72b-361ab04c76db | -4.29157 | -48.65 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed0a2ece-aa64-31b8-b19d-098c4eee7bbc | -4.29156 | -48.6066 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1ab97a4-6b44-3e02-b988-2a81bf57ee9f | -4.29087 | -48.6111 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3771bafa-5418-3bc3-af13-7f19d728d661 | -4.24821 | -49.18977 | 2024-10-29 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea701852-5e86-32ac-809b-1a4684a28bc0 | -4.22705 | -48.04482 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7aa468da-1d44-3597-9dd7-394641ef2c08 | -4.22236 | -48.04414 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0b6ac0d-740e-3ad4-bc16-f2a50b69cd7f | -4.19054 | -48.56629 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a640c581-c9b0-3c7a-8f76-fab1aa39c08d | -4.18666 | -48.5677 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b1b5e2a4-8a27-339f-8a41-f984794006aa | -4.18605 | -48.56546 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b05653fd-203d-304d-afd1-40250426bed9 | -4.186 | -48.57225 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 039b443c-f5e3-3eb2-8246-3bde6b0642d8 | -4.18535 | -48.57005 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49587a21-0326-3cc1-a909-24e528ec01ac | -4.11114 | -49.08419 | 2024-10-29 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99a0aa17-87ac-3372-a941-333025813729 | -4.10231 | -48.50716 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ea722eb-ae49-3199-8729-358a28a7557f | -4.10166 | -48.51162 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a20048a-e98f-3ec7-9c85-389285550fcf | -4.08008 | -48.30798 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45e6da81-1bf3-3c14-87ed-ff172cf57a8f | -4.07163 | -48.30172 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8f6fbdf-2c5d-3845-81db-92936c812066 | -4.06705 | -48.30093 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c538eca6-4715-37fb-9246-a4d9c10afb49 | -4.06316 | -48.29552 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fdbd664-f40d-3530-9675-8d4b3eebdda5 | -4.02084 | -49.00255 | 2024-10-29 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b502716-c06c-3c5f-a747-97f8659ea66c | -4.02021 | -49.00312 | 2024-10-29 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 80a5d911-27e8-3fce-8416-c9ab67444d69 | -3.9347 | -48.34558 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a05cb0f5-f872-3c55-8943-e9101803c737 | -3.93402 | -48.35018 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| de5bba55-d018-321c-a6fa-859d139f82e6 | -3.93334 | -48.35474 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 973c62fa-1872-3f10-9461-c02fa3191db5 | -3.93011 | -48.345 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 813ed1de-ae63-3f16-b3dc-481473a3850c | -3.92944 | -48.34957 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 33c21e45-3db0-3588-afc8-c039ac53c866 | -3.92877 | -48.35408 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d2d70727-b939-3222-b0e2-9a833cd3747c | -3.92556 | -48.34424 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6f4244e8-cc2e-33c4-bd67-d48054808db2 | -3.92489 | -48.34879 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6c1c31db-fe70-3609-a33b-ad439af17b40 | -3.9033 | -48.36884 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8d08ded1-c67f-330e-8fef-36348d8d24d9 | -3.90236 | -48.37134 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 63654a70-41a8-33c0-88ae-a722916e5996 | -3.83963 | -48.89577 | 2024-10-29 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 60c0f761-1ee0-374d-8d7a-222399f13338 | -3.83523 | -48.89515 | 2024-10-29 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| efda5ad2-7baa-37fa-afca-7f62519f8e83 | -3.83269 | -48.88192 | 2024-10-29 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 22f3f0cc-f1c5-347a-938f-f112e341caca | -5.79198 | -48.50183 | 2024-10-29 05:01:00 | NPP-375D | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bdd48bd-50f1-39c7-8282-f734dde3b448 | -5.70718 | -48.98127 | 2024-10-29 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cd6e5bd-af73-3a79-9502-303984117bf1 | -5.70269 | -48.98059 | 2024-10-29 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7def8983-3987-3efc-a8b3-f0ce78aa5265 | 0.08885 | -49.85635 | 2024-10-29 05:01:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80b62c9a-4cab-3240-9fa8-593a6ede9134 | 0.08408 | -49.87691 | 2024-10-29 05:01:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 537b46a0-ac09-3789-be32-14db0b2adf4a | 0.08334 | -49.8721 | 2024-10-29 05:01:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d194cd66-35dd-3ecc-a2ed-76fd7a2d968a | 0.07945 | -49.87268 | 2024-10-29 05:01:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9e6d1c4d-3557-3787-b9ca-e1c8fe29be87 | -0.23731 | -48.58478 | 2024-10-29 05:01:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6b3460c-3c50-342e-920c-01d9b86f3c14 | -0.2354 | -48.78988 | 2024-10-29 05:01:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 356e57e1-ad9f-3436-b4e1-53c28df71ff2 | -2.15314 | -49.65306 | 2024-10-29 05:01:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e657b426-12d8-37c7-9e91-85e7f99c2090 | -2.14853 | -49.65598 | 2024-10-29 05:01:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be309fc4-9776-39a3-a3a0-6521ac72b413 | -2.10143 | -49.6923 | 2024-10-29 05:01:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 547c5fef-e726-35f9-b95c-c092703f90bb | -2.03774 | -50.08474 | 2024-10-29 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9bc302c-b8b0-3c5f-a861-61fca2ccf034 | -0.86511 | -49.06138 | 2024-10-29 05:01:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f27cd73d-c4e1-3016-bea3-c7f053a587be | -0.86452 | -49.0651 | 2024-10-29 05:01:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bf589df3-0b7d-34da-a06d-da500e194def | -0.86038 | -49.06446 | 2024-10-29 05:01:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 81ec2405-c852-3582-a2b8-0bca9c3cc13a | -2.24027 | -49.73499 | 2024-10-29 05:01:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5ee4afb-4357-3b0d-99e9-d070ff9c12be | -3.25121 | -50.35776 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f865cc8-d063-3e39-9ee5-09d629c797ed | -3.21728 | -50.18123 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 35564c31-3d3e-310a-a1ec-efc2202fdd9b | -3.20718 | -50.38177 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5e61415-eaac-3004-bc90-e4add2287eaa | -3.1828 | -50.38314 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 02b70ca1-804c-3194-8728-4ff3c7ff66d8 | -3.18205 | -50.38817 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 5df8012c-98e5-3595-af92-cccc6b5fee46 | -3.1813 | -50.39315 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| f729180d-0d5b-338b-b979-e08332220b48 | -3.17887 | -50.38253 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 11947535-dd84-3979-909f-7c4c7e0f8df0 | -3.17811 | -50.38757 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 097b4340-c056-3aa8-848a-b4a0348831d7 | -3.17736 | -50.39255 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 206db5d6-65b9-3c36-808e-c02d0d07a4d5 | -3.17662 | -50.39751 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| aaac4e45-7f47-3d58-9ce7-0f0088b42026 | -3.17418 | -50.38696 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e30efa7b-e5f0-379d-8ce6-95ee9d4cc190 | -3.17343 | -50.39194 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 555df09a-aa4b-3acc-ba16-00cf69de3a9a | -3.16637 | -50.38899 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71a56e52-0695-34d7-b0fa-4d8eaeb04a51 | -3.15126 | -50.45952 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d3ce669-463d-31f3-97be-73f3b798c984 | -3.15082 | -50.46258 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73a74791-4fae-3c49-9324-bc0535f53376 | -3.14808 | -50.45398 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1d12680-d24d-362e-ac7d-81034a0220f2 | -3.14767 | -50.45706 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a024aa4-ef3c-364a-a9ea-379c310fe8c4 | -3.12455 | -50.34683 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 758b1899-a5f8-31b4-8c9c-1802d2a876a5 | -3.12148 | -50.36679 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03037b0b-3d06-3e84-9353-dfcd68814207 | -3.11984 | -50.3512 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9258c385-bd89-3663-acb2-809d20fe061b | -3.1159 | -50.35062 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3742fff8-9936-3308-a786-c7ff994ad24a | -3.07216 | -50.50578 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bacbe24f-6eb7-376c-96ce-0aa47340f225 | -3.069 | -50.50029 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 654dec60-8071-3a8f-907a-7409ecb18a51 | -3.06826 | -50.50518 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a0f03ad1-8147-3095-974e-532b426bd795 | -3.05451 | -50.41562 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7b80fcc1-cbbe-3eed-a713-f1d7cb956cd1 | -3.05352 | -50.41723 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8d792865-ddb8-3e3a-906b-ac13888c43a3 | -3.05058 | -50.41505 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7530510d-45b1-3e9a-83d4-0989277f40c8 | -3.04983 | -50.41988 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 28dc5022-3d9e-32f5-ab9a-343b6059d4d1 | -3.04959 | -50.41669 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b5f4d61a-100b-39ee-be48-5ef070bacd1d | -3.04666 | -50.41447 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1056e895-7b34-3fae-b94b-9915ee2ed75a | -3.04639 | -50.41124 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c4dd68a3-de8a-3872-8ed0-71619df40343 | -3.04589 | -50.41935 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 717b9e65-1f2d-3cf0-9401-059a1c4221ed | -3.04566 | -50.41614 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2782e614-4343-3802-ad27-2ed44e5494ca | -3.04514 | -50.42421 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 64891f13-3e3b-3811-bd95-bae2976c11af | -3.04493 | -50.42104 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 22598c50-f326-3d6c-80a0-c1966d29675c | -3.0442 | -50.42589 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 275dbdd9-db75-3955-bd6a-00e620d77061 | -3.04274 | -50.41388 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 55dd6a4d-d81a-3659-803d-63f8806352e6 | -3.04247 | -50.41063 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d3ab58b9-1626-3178-b56c-c7c198a917ed | -3.04197 | -50.41876 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2bb1c98d-fa15-3728-b3f1-670ffc57c715 | -3.04174 | -50.41554 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 486072e6-d797-3449-a064-d99afe116e55 | -3.04122 | -50.42362 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 61ce15de-33e2-3a1c-a558-1cb6dda18af7 | -3.04101 | -50.42044 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ec1384bc-4b2c-3867-a1ee-d37d12e0228d | -3.04028 | -50.42529 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e0d5eba4-e588-3ba7-9c1a-e27de7c11214 | -3.03806 | -50.41816 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15541c90-ed6a-38cf-869a-022b02dd6cba | -3.03729 | -50.42305 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7ae19be6-5e05-3a4b-81ce-615b711eb806 | -3.03709 | -50.41985 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db76da39-87e7-3f38-9258-268143a09fc3 | -3.03637 | -50.42469 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9e7bc44a-b0ba-38e8-9848-2650a1a62571 | -3.03413 | -50.41761 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README74.md)
