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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 647c48f6-1c27-3f36-9ad7-06821bd0e5af | -2.37151 | -50.49136 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 562b9632-25e9-3f00-acc8-ef019a5621eb | -2.36557 | -46.49298 | 2024-10-09 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6415ce1a-169e-3bc2-8bb8-c222ccf01868 | -2.36271 | -46.48873 | 2024-10-09 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ba98205-a67e-393a-8df3-555f14673f94 | -2.36214 | -46.49244 | 2024-10-09 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52101adc-1044-3a2d-9596-f29358805325 | -2.36157 | -46.49614 | 2024-10-09 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1deaede-6140-3622-b4a1-62ebe7555622 | -2.3544 | -48.99114 | 2024-10-09 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1965d697-0f8d-33e0-8047-67f79cf88335 | -2.35386 | -48.99462 | 2024-10-09 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b95cbc95-7860-32a9-8caa-5860e8ff31f1 | -2.35052 | -48.9941 | 2024-10-09 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d64adae-b9ce-3260-b7dd-4a58e983eecd | -2.34719 | -48.99358 | 2024-10-09 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e2d7d28-adeb-35fc-821f-98fa37c38950 | -2.34621 | -46.84223 | 2024-10-09 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d664803f-19cc-3b48-9224-4acfa8737243 | -2.34281 | -46.84171 | 2024-10-09 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 006ee077-c323-3cc8-b1dc-2e43de842e52 | -2.34225 | -46.84533 | 2024-10-09 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42a9f6d5-82dd-3a84-932a-9fa3f7b88824 | -2.34214 | -46.44769 | 2024-10-09 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1fed9f0-24be-300a-b6da-d155c21b21fa | -2.34156 | -46.45141 | 2024-10-09 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a760c49-6fef-3f79-a2cd-3f143bd45474 | -2.33409 | -47.97588 | 2024-10-09 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6fa56e7a-8f08-34f7-87d9-874da6bdeb50 | -2.33106 | -50.37817 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 774dfc43-67fb-3aa1-8cb7-ee8f633ff179 | -2.32291 | -46.72339 | 2024-10-09 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a32760d-94f9-3dd9-970a-c3327e22f495 | -2.32234 | -46.72703 | 2024-10-09 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edf02a41-887b-3e1d-af2b-495a3dee906d | -2.31893 | -46.72651 | 2024-10-09 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c44a7b0-dae2-3d20-941d-f710f8b13b52 | -2.30096 | -47.2415 | 2024-10-09 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 336fe295-2ef2-3c81-a61c-62e26f68a09b | -2.3004 | -47.24506 | 2024-10-09 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 606c1412-b863-3a2a-882a-fc8791045766 | -2.28278 | -50.54795 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39b07068-4d91-3de7-abaa-4dcd79e86c71 | -2.25769 | -50.57126 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2aca2ee7-ff84-37c3-b3ec-da962623de3d | -2.23912 | -46.74767 | 2024-10-09 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16c72407-4f9f-3149-aac2-7bac040192b6 | -2.23856 | -46.7513 | 2024-10-09 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dccb05fc-a8f5-3e3c-b928-49df78051c80 | -2.23799 | -46.75492 | 2024-10-09 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4794f001-1d1e-39f9-9dc9-8ee90009df5f | -2.23685 | -46.73989 | 2024-10-09 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c04d4666-28dd-307c-87b3-a5d4eca2ccef | -2.23515 | -46.72844 | 2024-10-09 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87553b86-f574-3ccd-8986-e27036af2126 | -2.23345 | -46.73936 | 2024-10-09 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ca28cf2-3255-3475-bcfc-038a70e57477 | -2.23248 | -53.65208 | 2024-10-09 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e59221c-2497-3e52-9997-5685340d2b15 | -2.23189 | -53.65575 | 2024-10-09 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9d8401dd-4236-3d34-b115-440d39489e96 | -2.2313 | -53.65945 | 2024-10-09 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0efae532-ed65-3576-b31e-5390a8d88916 | -2.23063 | -46.7575 | 2024-10-09 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17eaed94-cd77-38ac-9aad-679f25363cf7 | -2.22875 | -48.02339 | 2024-10-09 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46f7e437-5128-3e87-9047-1e4284abc4fc | -2.22836 | -53.65139 | 2024-10-09 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73452e95-b46e-3703-90c8-e6d8a6af05bd | -2.22777 | -53.65505 | 2024-10-09 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bdbbc4b1-879e-34d6-a828-3474132845b0 | -2.22717 | -53.65875 | 2024-10-09 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9962e9b2-3b39-39b7-8e9e-1a2970d1350d | -2.22607 | -51.81286 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9dd6825-c840-3abf-b087-d69d2d7f1b4d | -2.21276 | -51.87293 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf52c519-2585-382b-9df5-6b0e05e1836f | -2.20762 | -48.15802 | 2024-10-09 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8baebdb5-f9ed-32e7-9e90-a08dd3503fd2 | -2.20429 | -48.1575 | 2024-10-09 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfc5ebec-ee2c-35a9-b8ff-2f511ecf29aa | -2.19958 | -51.95597 | 2024-10-09 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0b69075-9a7e-371f-bd77-5f98c3a60b53 | -2.19233 | -48.5795 | 2024-10-09 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07622d85-d605-36e9-bb5b-7d3080996fa6 | -2.19199 | -46.0785 | 2024-10-09 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64db8ad0-ca53-3cff-807a-9e422d787802 | -2.19088 | -46.07932 | 2024-10-09 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9599773b-40ed-33f7-8fb1-5309c23ea986 | -2.18846 | -48.58243 | 2024-10-09 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 065e3848-2699-3136-8548-93166f6fc297 | -2.18472 | -48.82265 | 2024-10-09 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c49ad924-3afc-3c8b-b61b-129034e206f9 | -2.18417 | -48.82611 | 2024-10-09 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f1881e9a-2d12-3c2e-a11d-34b41434e584 | -2.14906 | -50.88699 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c399764-307d-371f-a61c-5291a958cb93 | -2.14554 | -50.88643 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0f96a7f-d23a-3c64-b759-602e247a01cd | -2.14492 | -50.89035 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9df80a0c-7a4e-3ec2-ae18-c26cce11bb2a | -2.14202 | -50.88588 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cdae628-f2b0-30a2-8268-ebac5b711be9 | -2.13891 | -50.70229 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96418cf0-96fe-3c82-b96f-615b052702c2 | -2.13829 | -50.70614 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5d1518f-7bf3-36e1-8287-12f1de0e07ea | -2.13541 | -50.70174 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dfdcbcc-5b21-35fd-9156-e9f23d80e5df | -2.12431 | -50.70395 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a86161e7-1f4a-3320-a6cf-4cad716f2521 | -2.11504 | -51.05569 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cd18965-bbf9-399d-91bb-e1d3aa98e7cf | -2.09246 | -50.67555 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3b66bcbe-0475-311b-99ab-8304f4cf1e79 | -2.08897 | -50.675 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 00700e6b-1d19-3b42-9152-7be885fa4118 | -2.07691 | -52.02473 | 2024-10-09 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c434164-3e00-3285-9683-3d8833a5c3ca | -2.07621 | -52.02917 | 2024-10-09 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ed067215-9d43-30b9-981d-65c46b047616 | -2.07318 | -52.02414 | 2024-10-09 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 354b286e-db2a-3994-a3ac-bdbaa44111cc | -2.07247 | -52.02858 | 2024-10-09 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5256586c-837e-31fb-be6e-c49972a71f79 | -1.55406 | -51.22952 | 2024-10-09 04:36:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 13546aaf-efec-3e11-acc4-da357cce4a8a | -1.95716 | -50.84602 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 75274cb4-0b81-38f7-9e44-a0e226f85251 | -1.8592 | -47.96588 | 2024-10-09 04:36:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a82c48a-31ea-3f97-b52f-c682a091b0cb | -1.84666 | -47.85067 | 2024-10-09 04:36:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e8380d8-1927-3c0b-b8df-559f0c071c94 | -1.84333 | -47.85016 | 2024-10-09 04:36:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7c0fe56-6730-3725-978d-71fbacf32307 | -1.78914 | -51.06464 | 2024-10-09 04:36:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63fd1290-b928-35cb-a89f-40c720cc9aa7 | -1.74063 | -54.24859 | 2024-10-09 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0713a7e-2e19-3751-af2c-7c54a1c402a2 | -1.66443 | -52.14306 | 2024-10-09 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fda9ace-e5a1-37cc-be33-bc3ea37000b2 | -1.66423 | -52.14055 | 2024-10-09 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b8ceeaf-f842-35a9-9e1f-439671ac9c59 | -1.63629 | -55.05222 | 2024-10-09 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3482b568-d378-3e80-8139-b26a3b4d6393 | -1.60556 | -47.38219 | 2024-10-09 04:36:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8eebc367-d44f-37e7-88f9-a79d9687d560 | -1.60222 | -47.38167 | 2024-10-09 04:36:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 365e50e9-af3c-3fc2-a912-2cfea3236641 | -1.55644 | -47.69518 | 2024-10-09 04:36:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5cbe921-213c-3607-88cd-10ab812d122d | -1.48502 | -47.33141 | 2024-10-09 04:36:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 959e19c9-882c-3adb-b3b0-46d6252fee37 | -1.46353 | -54.96313 | 2024-10-09 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19c10a92-306c-30c5-b4ac-4b55927fa1fa | -1.37854 | -47.49345 | 2024-10-09 04:36:00 | NPP-375D | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3978b2e5-2a85-3de5-b2c6-bb5968375ed0 | -1.3752 | -47.49294 | 2024-10-09 04:36:00 | NPP-375D | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 341a41e2-3e2f-3bb6-8d3d-710999d560de | -1.24106 | -47.89758 | 2024-10-09 04:36:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04d9d7f8-7101-3487-ac77-5a562cbfb214 | -1.23949 | -55.68269 | 2024-10-09 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11a338ae-20ef-3a5c-9cb5-10a34a68b2d3 | -1.23862 | -55.68806 | 2024-10-09 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e905d341-1b12-3c27-8d59-f89d4e542092 | -1.23774 | -47.89706 | 2024-10-09 04:36:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a5227e6-21d8-3574-bab3-e33725ebfc23 | -1.19702 | -54.22094 | 2024-10-09 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dee65f47-7daa-30c8-89d6-a87ae67cf9a3 | -1.19638 | -54.22503 | 2024-10-09 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6807ccf3-a28d-3be8-b719-0c12446c392c | -1.1918 | -47.47834 | 2024-10-09 04:36:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 140ec3a5-a5ca-329c-a2f7-b388b2bb42f7 | -1.18846 | -47.47782 | 2024-10-09 04:36:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 66d4e30b-39bf-3d57-8eca-2285b84c61c4 | -1.17144 | -55.71284 | 2024-10-09 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df8fa251-df32-3736-a163-8cc0abc485b3 | -1.16921 | -54.14387 | 2024-10-09 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 032cbd09-af67-3527-b093-23633cb07a86 | -1.15872 | -53.78288 | 2024-10-09 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac424b17-9497-3a7d-acc3-ac76a4ca35a7 | -1.13606 | -54.21119 | 2024-10-09 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba941d43-1573-3ac2-a543-844e0242a50b | -1.13438 | -54.10595 | 2024-10-09 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64cc39f5-8735-3e0b-9a65-98cf541845d3 | -1.13375 | -54.11 | 2024-10-09 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b866083a-bed4-3ec1-9984-75bfccf9fbad | -1.13006 | -54.10523 | 2024-10-09 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69b2f6bd-c49c-3c2f-b84e-01e29429b9d6 | -1.12945 | -54.22366 | 2024-10-09 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bd9a88d-8726-3bad-ab0c-865245007618 | -1.12943 | -54.10925 | 2024-10-09 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ab54805-3aa6-3d75-a3e6-a45e618afa45 | -1.12553 | -53.63937 | 2024-10-09 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d77a6eec-bde1-3784-ac34-70c06fd63b2b | -1.12354 | -53.70508 | 2024-10-09 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9eee55a1-afe6-366d-be73-5cc9fd450d4c | -1.1214 | -53.63832 | 2024-10-09 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README112.md)
