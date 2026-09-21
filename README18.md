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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef99cc02-93fc-32b5-ad86-ae5a7e421b0c | -3.0534 | -61.2767 | 2026-09-21 03:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 5db4cf06-9e07-3654-a9c4-395824be620b | -7.5703 | -57.6962 | 2026-09-21 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| d0eebe35-ab2e-33d6-9aa7-7ccbceb88069 | -6.2026 | -57.7778 | 2026-09-21 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 7e7282a9-295b-39f2-bcad-d8f7b65fa0e7 | -16.0495 | -52.5106 | 2026-09-21 03:20:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 700861b9-dbba-386c-93ea-fab1275ffd38 | -3.41002 | -39.28447 | 2026-09-21 03:21:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f96a6ac8-3b4a-3d26-83bd-2519763c6285 | -7.43516 | -44.77724 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 10883b8f-4521-3561-bbef-4d0fe4bc5b1a | -4.00473 | -38.98548 | 2026-09-21 03:23:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 77090cd7-c105-338b-8ddd-e88df1c3c444 | -8.75891 | -44.28001 | 2026-09-21 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 534f2665-8505-35cc-9825-d614581ccad1 | -7.41713 | -44.77431 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 36.8 |
| c8403cca-264e-32a6-ae9a-fb34eb46824b | -7.45222 | -44.74375 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1428f5d8-3ca3-3c10-8afe-3c25a2a6835c | -7.43854 | -44.77768 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5315b35f-e029-3fab-a565-0753ae952390 | -9.60516 | -40.6199 | 2026-09-21 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0c5a36da-d6f9-363d-aed5-cbbe4da280c2 | -7.42803 | -44.77608 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 24b5dc6e-7505-3419-b091-2b463c948ec7 | -7.4217 | -44.78906 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 37.8 |
| fbe6a1d5-b0df-3472-b51b-9b338f37caaf | -7.42669 | -44.78299 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 64884869-f945-3ff1-a449-8c7a51a1ea46 | -7.42087 | -44.77509 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 595a67c9-a786-33f5-af24-9c4b743968ad | -6.68603 | -35.08729 | 2026-09-21 03:23:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 7480e2cf-49ce-3c76-a0f1-a918f0502685 | -6.91559 | -43.72728 | 2026-09-21 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae984cad-c1c3-35d2-b8ad-241d8941e84e | -7.45039 | -44.73655 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e9e0b54b-cefe-39a6-a233-2a9c2a0619de | -4.00526 | -38.9823 | 2026-09-21 03:23:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eae72861-b7ac-3f8c-be57-afd85d94cbec | -8.76686 | -44.27516 | 2026-09-21 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b9ce0227-ce52-301a-b22a-d5d193cdd610 | -8.39129 | -37.64825 | 2026-09-21 03:23:00 | NOAA-21 | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ef088c0b-fb3b-301b-bd62-66da7336262e | -7.42936 | -44.76927 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 20b1546a-d2fd-3d33-97bc-ef2349b8b804 | -8.0062 | -44.81388 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8151fa96-e806-34d3-ae0b-28e90e0d5a6c | -3.99892 | -38.98799 | 2026-09-21 03:23:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7955b5f5-154b-3407-98aa-488179d848b1 | -8.78103 | -44.28514 | 2026-09-21 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bfebc732-a7a0-3996-8632-015838a7f56c | -8.7743 | -44.28375 | 2026-09-21 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7d4ff2b2-a40e-3732-ae63-3871f6e1511c | -8.01334 | -44.81472 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15cd9ab1-ad44-3e1d-8020-3f3ddad86ddf | -7.4437 | -44.7501 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3cedd884-fb62-302d-af54-5d0197188116 | -7.43268 | -44.76977 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c395f4ec-f54c-3de0-8eb6-7144b6d23e94 | -8.77669 | -44.29685 | 2026-09-21 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c1f3d7d3-f8b9-3f52-b758-f8e6a7ef0830 | -7.44096 | -44.78524 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbff7433-4158-35a2-ba51-210b24bba15f | -6.90656 | -43.73827 | 2026-09-21 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 58ef9b94-6b16-3d05-ba7e-73498ccb2ede | -8.77361 | -44.2765 | 2026-09-21 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3369ca16-f715-3e31-84d5-96a1d3520627 | -8.78034 | -44.27791 | 2026-09-21 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ddc2686f-2335-3e1b-aba0-e5ed191d9de3 | -6.9077 | -43.73217 | 2026-09-21 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4559f720-28e1-375b-977f-4375fc2eddeb | -7.44904 | -44.74355 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5b69d3d0-4f1f-3d1d-a007-30e54ec2b5ee | -7.43725 | -44.78453 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ed603a42-a713-31bd-a737-25f2d670a6f9 | -9.61112 | -40.61747 | 2026-09-21 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9c2ea5b5-df2f-350a-90ee-e566ba46e9b9 | -4.83012 | -43.52314 | 2026-09-21 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 22ecea48-643d-3882-9a23-d6757667de46 | -8.77553 | -44.27758 | 2026-09-21 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 584e2768-6dbf-3dcf-8c0a-3424b5ad4fac | -7.41507 | -44.76712 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 5392af32-a51a-3c3c-97df-f4c89b5e020b | -7.02428 | -42.08382 | 2026-09-21 03:23:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ae2598da-4960-38bf-a509-2ae8863aaddc | -8.77242 | -44.28267 | 2026-09-21 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c343aa59-7e75-39c8-909f-82b1f6d73a62 | -7.41842 | -44.76748 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 528bf9e9-d7aa-3dfe-b6fa-249bcc63389d | -8.75769 | -44.28632 | 2026-09-21 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c364660f-7134-30dc-a475-190a30f99658 | -7.43383 | -44.78409 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aefbc2aa-7581-35ce-bf81-ec5667768aab | -8.77848 | -44.29793 | 2026-09-21 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 54d2d98a-82de-35e0-bd61-cfe53b5930f6 | -9.60675 | -40.62151 | 2026-09-21 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 50b468d3-360d-3d3f-908f-fda028435e29 | -7.4222 | -44.76828 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 3895b8c4-b213-3f99-8594-55f958f61304 | -7.41954 | -44.78189 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 4217ecf8-9057-39a5-afec-cae758979e9f | -7.43141 | -44.77649 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| e279e639-6c26-340f-9ff7-218599de9fab | -7.88586 | -44.84588 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 82ed21c0-5f43-3877-af3e-3b8d1b482509 | -9.61048 | -40.62086 | 2026-09-21 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b259320e-3693-3fad-a11f-578bc20896a2 | -7.41373 | -44.77398 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 77025c86-3ede-34f3-b34b-2af7d75e2261 | -9.02674 | -44.91597 | 2026-09-21 03:23:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47a92088-e0cc-39ca-b79f-5662271cf079 | -7.133 | -42.07811 | 2026-09-21 03:23:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 767c8f88-b284-3de9-8f47-7f09d3934a41 | -7.12776 | -42.07236 | 2026-09-21 03:23:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ea85ae15-eea0-31cf-ae07-6ea619371728 | -7.43596 | -44.79144 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fde35d81-0d7d-3f8c-a9fa-fd46b5854694 | -7.43962 | -44.79213 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4432fbd6-6a97-359c-98b6-8b29892cd5bf | -6.36092 | -43.36692 | 2026-09-21 03:23:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7e0d084e-ff02-38ea-8bed-96ceb1966dda | -7.42427 | -44.77539 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 40cec082-8823-3a62-9e0f-7a66376b1b2a | -7.44768 | -44.75056 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5064cfa5-8003-3649-b6d3-6635252cd176 | -7.44046 | -44.74991 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 02e1ecd6-dad6-3fa7-9057-30af983312c5 | -9.01975 | -44.91472 | 2026-09-21 03:23:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82c0060e-156a-35d0-aab3-7826ea52a9d6 | -8.76312 | -44.29449 | 2026-09-21 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5919b0a8-ac8b-3ff9-b3db-b3e2702fae59 | -7.15371 | -39.33829 | 2026-09-21 03:23:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1208b63a-36a6-3b37-a5c3-f426a912e66e | -8.77979 | -44.29135 | 2026-09-21 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d4434a01-0c07-3f97-9678-07f2fe6f27c0 | -6.37567 | -35.1601 | 2026-09-21 03:23:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 215b30c4-cd89-3056-a021-56cadd5b6d72 | -3.34183 | -42.76889 | 2026-09-21 03:23:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 839b9910-5c02-34e7-b89a-88404a493f8a | -8.77915 | -44.28406 | 2026-09-21 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ff8f44eb-dca4-3a4b-aff7-344d9620c40f | -9.02545 | -44.92243 | 2026-09-21 03:23:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 033ee5f3-935b-39a8-86f5-874a2b648bb9 | -7.44501 | -44.7431 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b9da8162-e229-3c6c-a66d-9b660e040522 | -8.77795 | -44.2903 | 2026-09-21 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 284d39da-de32-3523-8021-a68916c8df84 | -7.42556 | -44.76857 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1022445d-8c9e-3e57-a2f8-0778e34150fe | -7.34436 | -44.46985 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dcf3694a-0a71-3419-8b6a-9a418304b9f1 | -3.99946 | -38.98476 | 2026-09-21 03:23:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bf03cc17-8122-39b5-a021-2a3613a42c43 | -8.76009 | -44.27393 | 2026-09-21 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 867434fc-f795-3bb7-80d3-cb588e0ee1de | -3.34285 | -42.76299 | 2026-09-21 03:23:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b769083-405b-357f-9566-a4ded3284f68 | -7.45352 | -44.73679 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a4becfd3-5e98-3707-a8d0-e973582dfef5 | -6.91445 | -43.7334 | 2026-09-21 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9accfba0-1295-3873-850a-284ec9aec888 | -7.42298 | -44.78225 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| fa9e17a7-d909-301c-898d-a2e4872cf790 | -6.37648 | -35.15521 | 2026-09-21 03:23:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9c27efd5-652e-3beb-a761-5a5868faccfd | -6.92116 | -43.73478 | 2026-09-21 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c913b8a3-66bc-3ff5-b333-37c9e1254d50 | -6.36205 | -43.36078 | 2026-09-21 03:23:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 293dc625-0bb1-332b-8041-2494ecb5cf2f | -7.41821 | -44.78872 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| cea481a9-c393-3859-99a4-232ecdae4f30 | -9.60736 | -40.6181 | 2026-09-21 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f9f17b12-6e53-328b-bd13-eae25b37bf98 | -8.73555 | -36.82721 | 2026-09-21 03:23:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 911e642b-22fb-3b99-ad74-78bde8d420b2 | -8.00507 | -44.81968 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4b663352-938d-31d6-81d0-dbdc641a1adb | -3.3408 | -42.77486 | 2026-09-21 03:23:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1f9864f-9aa8-3149-98e7-7abd1da6d6a4 | -7.43644 | -44.77064 | 2026-09-21 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f4109885-563a-31a8-bcd2-aa008d636cef | -6.32423 | -43.37923 | 2026-09-21 03:23:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9df9a9bc-2b07-3751-a388-18eb3e15cd44 | -9.45064 | -45.39729 | 2026-09-21 03:25:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b02b7e05-6b08-320e-b8e2-b36baba6ce5b | -11.67519 | -43.44345 | 2026-09-21 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 337efd18-6fcc-390d-ba61-0f124346dffc | -14.98285 | -43.08986 | 2026-09-21 03:25:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 71caff76-dd18-3212-a508-0fb4d2afaf8a | -15.52099 | -42.65689 | 2026-09-21 03:25:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| cb7c1ea0-4d5f-3cae-8fe5-0f9084a37cf0 | -14.23081 | -44.64062 | 2026-09-21 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c1b37c9-bc26-305f-ba8a-0b7f83446aff | -11.15549 | -42.83203 | 2026-09-21 03:25:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8d5227f4-bf79-37e8-974c-c2161f6c73b5 | -13.28855 | -43.54824 | 2026-09-21 03:25:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 371a1efb-3079-3684-8188-a9a73211aa80 | -9.44613 | -45.41945 | 2026-09-21 03:25:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |


[Clique aqui para ver as próximas entradas](README19.md)
