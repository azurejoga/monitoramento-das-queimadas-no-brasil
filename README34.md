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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 571bb0e6-d751-3e36-9f55-d0ea29940485 | -22.26089 | -47.04522 | 2025-08-19 04:32:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2e54ad0-48da-3e03-8399-2329b799d66b | -6.9715 | -43.5833 | 2025-08-19 04:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 3c64fc0f-1165-302f-afbb-71d3401b1e29 | -6.9527 | -43.585 | 2025-08-19 04:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 6953c3fb-bcf6-322a-b702-f3ece64ad775 | -6.9339 | -43.5868 | 2025-08-19 04:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 5c9cbdfe-2fd7-3676-a0e9-ce83ee7f3e16 | 2.46268 | -51.24339 | 2025-08-19 04:49:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5288e1b1-e372-37cb-a8e1-daa69ca507b4 | -6.9339 | -43.5868 | 2025-08-19 04:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 18a44bc8-ecef-3fc1-ae4e-f846d46fdb88 | -6.9715 | -43.5833 | 2025-08-19 04:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 72acf978-471f-3dcd-8e50-f24069861c14 | -6.9527 | -43.585 | 2025-08-19 04:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| dcbc4d84-04ea-3f9a-adc9-0b2418ee1746 | -6.93651 | -43.60043 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfb13317-bbd2-3897-9543-68c0804ab890 | -6.05752 | -43.74592 | 2025-08-19 04:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed19e334-8adf-39cb-bba5-c271508cc2e9 | -5.64805 | -43.40429 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca63fb36-179d-3aa3-82b7-2ca427881698 | -6.95775 | -43.60334 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6f6a3b39-d97f-3063-9e86-2d2d9993af6b | -3.45628 | -48.96778 | 2025-08-19 04:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac8e30bd-f963-3d6c-92e3-60bb6b5c6cba | -3.44558 | -48.96616 | 2025-08-19 04:51:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2195183-f59c-3b1e-9fe7-90c74386fcd4 | -5.64635 | -43.40665 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f0eaec3-0e9e-3cb3-b703-44f8b800621b | -3.08549 | -48.85352 | 2025-08-19 04:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c286ceb-906a-334e-bab6-798da9496873 | -5.97496 | -44.29294 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 84e48e3b-32fb-3ffc-9c1f-a137ba4617ca | -5.65134 | -43.38195 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b22232d-e7c8-30a5-a885-525b91fb1a0c | -5.64991 | -43.39164 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4f73667-aad7-35bf-b042-5cf1f23e36b0 | -5.64851 | -43.40112 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 859eb3bd-638a-3b22-ab9d-128d7744f62b | -3.64475 | -43.95574 | 2025-08-19 04:51:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e71e9fda-d2b0-3474-b539-7883d19a7b6f | -3.97744 | -42.51263 | 2025-08-19 04:51:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 079eea78-f56c-3c97-934d-e5d11da30d61 | -5.97693 | -44.13363 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17256856-a407-3667-9894-546c79a0bfa5 | -6.06565 | -44.12588 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f95945f7-0b9d-3f02-be1c-a95fdf1760ed | -3.37908 | -52.71704 | 2025-08-19 04:51:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1401cdfa-e237-391e-b9d4-d2f285f2f684 | -5.36786 | -46.30323 | 2025-08-19 04:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd476816-5ca3-3bea-91d9-eb7bdfbd1a4f | -6.97111 | -43.58531 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7dc16b60-11a8-397c-8b44-44680b92ffee | -6.54748 | -43.0097 | 2025-08-19 04:51:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95da82aa-d93f-3504-a66d-73c5ebcca173 | -6.93074 | -43.603 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f37a04f-ce04-385f-8610-c45a4338798b | -6.74876 | -41.54707 | 2025-08-19 04:51:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 43824c25-c085-3e4a-a497-fd637f59afad | -3.9829 | -42.51349 | 2025-08-19 04:51:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b8961bca-1999-308f-a1c3-a901a5bfc3bd | -3.98734 | -42.52134 | 2025-08-19 04:51:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 768742d8-55a2-313d-bb3f-02e7a44a14f2 | -6.94714 | -43.60181 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 600248ab-d18a-3c6c-9050-7d7f84521dc6 | -5.78893 | -43.60916 | 2025-08-19 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ad32dcda-6d46-33a5-8d27-7632740afe83 | -6.94484 | -43.61833 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2737e947-09a6-3fe6-bd8f-e953178ab908 | -3.97147 | -42.51526 | 2025-08-19 04:51:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6948cc4a-3c91-3046-b06b-4d1f5731f0a0 | -6.74396 | -41.53717 | 2025-08-19 04:51:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0bb784e8-fe31-39ac-a267-63c50b8f737d | -5.89962 | -45.53812 | 2025-08-19 04:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f45fafb-be81-3190-a908-143067284860 | -5.9723 | -44.12993 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a28b05d1-35d1-3ef0-9900-9b0f94acbf6b | -2.54071 | -47.72351 | 2025-08-19 04:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f49ad49e-4ab4-30e3-85ee-7b5749c9caa0 | -3.37573 | -52.71651 | 2025-08-19 04:51:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4afedb00-4c74-3aee-817b-5d08abc2cf81 | -3.04499 | -49.43613 | 2025-08-19 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4a2d9f4-1d2b-3314-9e95-dbb450efc284 | -3.44943 | -48.82136 | 2025-08-19 04:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f8ea12c0-f31c-351a-b602-91eb842b406e | -6.85327 | -44.41744 | 2025-08-19 04:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d530bbde-e225-39ca-87af-13a5190e3526 | -6.96003 | -43.58704 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| fc81417c-7234-3898-8bc4-2c4634b9b367 | -6.55366 | -43.00811 | 2025-08-19 04:51:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0174c2a1-df08-357a-b3ae-10691a44f68e | -6.94182 | -43.60112 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 036953fa-c2ab-3a03-800a-e64db4d43807 | -4.27735 | -48.18978 | 2025-08-19 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e71e5cce-cbe2-3671-8b61-f161d5e86b0b | -6.37473 | -43.31746 | 2025-08-19 04:51:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0d841a7-1779-3cb4-a6b8-d377e2f55cba | -4.59183 | -43.31789 | 2025-08-19 04:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c7cec91-4b1e-383c-af6d-e74bed5db094 | -6.94138 | -43.60433 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9ac3747-ae6b-3f3e-8cff-dc96322c5195 | -6.95681 | -43.61002 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bbd196a5-cb8c-31b0-9eee-0027543cef67 | -6.97064 | -43.58865 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 99289440-e842-3d71-a3c0-465f559ae1b5 | -5.97074 | -44.28678 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 94de94fb-4d6b-31c2-9394-6f54936a66ea | -5.78994 | -43.89169 | 2025-08-19 04:51:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4f6130d-2d01-3ea6-8335-43d23d608fec | -2.54518 | -47.7195 | 2025-08-19 04:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bef0071-6a04-3cab-97ea-af190700bae7 | -4.01935 | -48.06249 | 2025-08-19 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e565c131-af6d-3bb2-81fa-00dd5bdb3121 | -6.15888 | -47.27769 | 2025-08-19 04:51:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1defda9-c1a7-338e-a1b6-f53ca3703491 | -3.98188 | -42.52048 | 2025-08-19 04:51:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a08f649e-4124-35c3-b939-16c14810c4a1 | -7.16749 | -43.51014 | 2025-08-19 04:51:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3ae89b07-0cca-3a34-a615-1a0a7111b2b5 | -6.95198 | -43.60587 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 842f8a6c-ee0c-319f-8b34-5a1eb8630360 | -6.95865 | -43.59691 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f6127da4-2227-313f-9bab-9eda98662387 | -6.55893 | -43.00783 | 2025-08-19 04:51:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50bb9988-db41-36c1-beaa-76a7cf04431b | -6.95728 | -43.60666 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8cd7e0d3-63e4-33c0-bb04-6ffad2f73a72 | -4.92278 | -43.24905 | 2025-08-19 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93a9d5af-77df-371f-86b2-34368fc619bc | -6.94092 | -43.6076 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06dd799e-c7a7-3026-923d-eaef603057ff | -4.01559 | -48.06187 | 2025-08-19 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe8fd476-ad53-37bb-b954-4c9817f9728b | -4.59256 | -43.31496 | 2025-08-19 04:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db2658fc-265a-3673-9063-bf046bcd05cf | -6.55285 | -43.9845 | 2025-08-19 04:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4838104f-7bd6-3134-b8dc-e4d55ecce2cf | -6.92985 | -43.60946 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e89f274d-88cd-3855-a94b-f3465f9d70df | -2.58863 | -51.92293 | 2025-08-19 04:51:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8e5cabe-038c-3b97-b0aa-0be0b5a66ebb | -6.87708 | -45.20317 | 2025-08-19 04:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d462b93-e625-3f3c-ab9a-4950272d0a82 | -6.93741 | -43.59392 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3ac837e-cfbc-391c-bbd3-614ef6ccab32 | 1.0923 | -51.31429 | 2025-08-19 04:51:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1750ebcf-d76b-3942-877c-6644bf9401ed | -5.7866 | -43.89299 | 2025-08-19 04:51:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96f5084d-25ba-320a-80b8-8e5199fd7133 | -3.97693 | -42.51613 | 2025-08-19 04:51:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7c7813b5-063b-335e-a762-924ebe2f6bf1 | -6.94803 | -43.59539 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 941a0fe8-18f2-341b-b762-27db05d20a95 | -6.94758 | -43.59861 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d09ac0e-d280-3ad2-b848-ba1394928f0d | -4.92269 | -43.24567 | 2025-08-19 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2225e3f8-37d3-306b-a8ed-d00da10e2a8b | -4.91846 | -43.24187 | 2025-08-19 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0e873e83-c042-3ec6-9505-92401d08b0e8 | -6.4523 | -44.55778 | 2025-08-19 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 497c87a3-7d4d-30ab-ae29-49f5b0f0c10d | -6.74271 | -41.54612 | 2025-08-19 04:51:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 28404f18-53bf-32f8-bd5c-e59ae90e4d0b | -6.94364 | -43.58804 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2b1d9fef-6fbc-3946-9ae2-3e4a86d5488a | -6.93695 | -43.5972 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b74a3002-6af9-3726-887a-675255159bdf | -5.64901 | -43.38758 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1353c49f-4d98-381c-a4db-75de958c3cf2 | -2.90812 | -48.29428 | 2025-08-19 04:51:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a17cbfae-ac7f-3b5d-8b15-36464855db67 | -5.92181 | -46.00057 | 2025-08-19 04:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 382a605a-4fb6-30cb-8098-a605cd43fdd5 | -6.93787 | -43.59058 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 99e30157-6762-3450-97b0-44fccd82b908 | -6.94575 | -43.61174 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8d9c676-8a03-3ba8-ae6a-3f5abcbfe505 | -4.59135 | -48.78223 | 2025-08-19 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2f1ad80-a36c-3982-a620-02ebc0ee785e | -6.93606 | -43.60366 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7a6514f-e946-3202-af0b-2ca2382fe44a | -5.57712 | -44.084 | 2025-08-19 04:51:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7b02feaf-3902-3ba1-8feb-a00d91186c38 | -6.67983 | -43.68148 | 2025-08-19 04:51:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11662925-b15c-302d-b093-2c555770acc0 | -6.51564 | -43.44383 | 2025-08-19 04:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7b94b4f7-2f65-3706-ac27-47ea50c47da1 | -6.06485 | -44.13137 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fea463de-dced-3f06-ac58-03a11cb14b58 | -4.54155 | -46.68213 | 2025-08-19 04:51:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08375d62-6fce-350c-afac-0e67679570b5 | -6.96351 | -43.60089 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ca3daaec-81ec-34d8-8997-4a0605fa79b5 | -6.51672 | -45.48914 | 2025-08-19 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42631341-c701-3709-b1b1-5a0217f61ee3 | -3.74045 | -48.93076 | 2025-08-19 04:51:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c1ac960-687d-31c6-8e48-0d760ca14a6b | -3.98785 | -42.51783 | 2025-08-19 04:51:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |


[Clique aqui para ver as próximas entradas](README35.md)
