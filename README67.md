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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb479a8a-a681-36ec-969c-a599be6f8915 | -1.10805 | -53.33252 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7ae1bf85-9a03-319d-b60a-bfc774df43d2 | -1.10792 | -53.35701 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 48239980-ecd2-33f4-ae94-2945e2d13ac1 | -1.10731 | -53.36097 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c84c83b6-ce97-31a0-ba4e-f03191fbc9a4 | -1.10713 | -53.34595 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1839bd22-aca2-35a7-98c5-7ea42cc0f5a7 | -1.10675 | -53.32545 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbe5ff3c-b3a3-3b1b-9c10-9d87c5ee8e0f | -1.1067 | -53.36494 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 4d60b824-6164-3873-a03d-457f9f168eb7 | -1.10649 | -53.34994 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eb6a1348-7456-393e-8d6b-abeb9b5b6869 | -1.10621 | -53.34452 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ae34f791-aa26-3156-be7e-be3cb03a9f79 | -1.10611 | -53.32947 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 650b16af-f715-3962-8f64-356c74b3e491 | -1.10608 | -53.36892 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| dd2b911b-4e7d-3f20-b4ed-b15ade43023c | -1.10586 | -53.35393 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d6475829-fb01-310e-b945-be375149dcb6 | -1.10559 | -53.34851 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ad03d431-1e3a-3bd1-a371-ef7300da9246 | -1.10547 | -53.3729 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 941bf8c1-cceb-32d7-9709-21b29f287178 | -1.10523 | -53.35788 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bb82cf98-bd7c-3929-8157-b5c4be9728d0 | -1.10511 | -53.328 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f6086261-dadb-3ecf-8280-36ad02f0eebc | -1.10498 | -53.3525 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d1e8ffe-936a-37e5-b244-59bc0f28ef40 | -1.10485 | -53.33745 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ab8a6b7c-0c4d-39db-990a-8544368593ad | -1.1046 | -53.36183 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 390a05dc-6096-378e-a5f1-b96535678a70 | -1.10437 | -53.35648 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8fef3b50-a1f5-3ff1-ab8e-817a38ea9918 | -1.10421 | -53.34144 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ca3e7467-0be6-3200-a7ae-9526bff1727e | -1.10397 | -53.3658 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8f3b6d5a-3c8d-38f6-a33a-df8f99e4750a | -1.10388 | -53.336 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f6801947-cd50-397d-b629-45eeb7964c49 | -1.10376 | -53.36043 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1cf7fe86-f34b-3510-831a-2d17d10366bd | -1.10358 | -53.34543 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 083c08cc-6ebb-3a54-b6ef-f57fff65dbea | -1.10334 | -53.36977 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c88255d3-21af-3151-b8df-5c974259d1d8 | -1.10327 | -53.34 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dd7767a7-bca1-361a-8b47-f07cf0d49cc2 | -1.1032 | -53.32493 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 985d5b11-5110-3233-8afe-08d4bea764ff | -1.10315 | -53.36439 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ae040142-243b-38be-85cc-17189bad8e0d | -1.10294 | -53.34941 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c8cca16e-986e-3175-b73d-70e302895f97 | -1.10271 | -53.37375 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef34981d-3e5f-3f97-845f-5927dc1fbe17 | -1.10265 | -53.34399 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 72592b8e-be7e-3bf6-80dc-7c6bd57024e5 | -1.10256 | -53.32896 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e962d246-e6e9-332e-8f10-f4388d3513c0 | -1.10254 | -53.36838 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5cee18b5-a098-3e4f-9c5c-96f1020b3dcf | -1.10231 | -53.35339 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3ec8fd69-4010-37dc-a99d-f7f373b16b54 | -1.10204 | -53.34798 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 636b47fc-dfe9-331a-b3e8-6646283502cd | -1.10192 | -53.37236 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a6d1027-7066-3da8-9cd8-fb92b82af3ef | -1.10192 | -53.33294 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 468a26f6-85f0-39d0-8a78-acf02360e541 | -1.10168 | -53.35735 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8f5d1e00-bed3-3667-adf3-920bf80c5d27 | -1.10143 | -53.35196 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b6d90eaf-a41f-31d9-9b3b-a8ce277d7bcb | -1.10129 | -53.33692 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 29681306-b8c4-3dc5-aceb-8c50600c282d | -1.10105 | -53.36131 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3322d78e-3283-3699-9658-ce2216820f5e | -1.10082 | -53.35593 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 53c0d5b6-2370-32fb-8a44-f4df30993fa8 | -1.10066 | -53.34091 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7cdf2dc2-14d6-3eb6-bcba-0cdb9fd91e92 | -1.10042 | -53.36528 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7eb3e72a-732d-36d3-9701-de71a45b7b69 | -1.10021 | -53.35991 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 883883d8-b2e6-3e85-b51b-65bac9449bae | -1.10003 | -53.34488 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b1963592-a762-3aef-8d35-443311fc935d | -1.09979 | -53.36924 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 48308417-39a0-3dc4-ab1f-d40ebb11549b | -1.0996 | -53.36388 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5a37d3d2-5f18-3d5c-af92-4b047dcb8127 | -1.0994 | -53.34886 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1d8314fa-8b61-3849-8978-27287721ce55 | -1.09899 | -53.36784 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 45f04e9c-5ce5-3cc2-9054-2050caa46f7f | -1.09876 | -53.35283 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6c0f0064-ffcd-336b-8ca9-d5c4cdbb1407 | -1.09837 | -53.3324 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b364b86-0794-3f2c-8566-85090bcf136a | -1.09813 | -53.35681 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 143ec488-edba-3b66-acc1-15e5ee0a0cc8 | -1.09774 | -53.33639 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4ba1c0d7-20de-34a7-960f-5b5f892914ff | -1.0975 | -53.36079 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f85af75-dc16-3da8-9fb0-e2a16c09894b | -1.09711 | -53.34037 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| df73bb55-49a5-375e-8951-7a24b725f892 | -1.09687 | -53.36475 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b1caa65-9b46-3e24-9e9a-c1b6fceb5b1f | -1.09648 | -53.34434 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 87fd530f-8f5d-3f88-aa48-200b4a1cea12 | -1.09624 | -53.36871 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e57a12a4-2d17-3188-9ebb-b419580ee368 | -1.09585 | -53.34831 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 330227bd-9f52-308f-a9f3-5a4621da8117 | -1.09522 | -53.35228 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e95ea49c-9646-31e8-924b-43e4358a2115 | -1.09269 | -53.3682 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21127fa6-3e23-3760-93f6-a38b44e9a585 | -1.08525 | -53.27713 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 121b90c4-0543-386f-81c5-07a1944c18f4 | -1.08462 | -53.28116 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84a6374d-61af-301e-8989-ab0ead6e9a36 | -1.1811 | -54.57318 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fba631e-6d17-36ec-a50f-270797369832 | -1.17715 | -54.57623 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e60928f8-2d29-3183-92f9-de2e72335b2a | -1.17659 | -54.57983 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f77a8b0-af50-387e-9118-155f1b2ae18d | -1.1749 | -54.56845 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a2cfded-617b-352b-8f8d-552861b85aac | -1.17377 | -54.57566 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bb4cf424-ed91-3499-9be6-a70a43a6acf8 | -1.17152 | -54.56788 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 179ec85c-65e4-3b34-9909-f05668daf291 | -1.16813 | -54.56734 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1d686be-3e0f-387c-8d59-f586376b97d6 | -1.16756 | -54.57094 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 880d1292-31f5-3179-9721-216a65b676de | -1.16417 | -54.57042 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2727d281-2598-3d73-8dd5-1b15dc8d3869 | -1.16362 | -54.59618 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7728241f-ac29-3bfd-9275-d22b6031543d | -1.16249 | -54.62555 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e076052-86b0-3e01-9040-75a0207e99ff | -1.15684 | -54.59513 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8211349-2f9c-38ec-b0fa-7d9d28e7437d | -1.15628 | -54.59874 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e536166-ff9e-3a1e-a1b2-166b174fb3ff | -1.15345 | -54.59461 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42addb45-2f3d-329a-aab7-1caa10a57963 | -1.15289 | -54.59821 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a41f7d4f-c6a2-31f0-a9ea-1617d409b9e3 | -1.14502 | -54.1823 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 741ed5a7-4f2d-342e-868e-1657a3e92d44 | -1.14159 | -54.18178 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e74e1d4-2b9e-3c47-94df-bf5fb68cc277 | -1.94168 | -54.93806 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd285608-e52b-3018-81d0-915c4f5f7fa5 | -1.69995 | -54.65167 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d66d6dcf-46e0-3eaf-a618-459f5ece0cb5 | -1.39203 | -54.16657 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| dd3bf124-5ebf-3733-a986-730896b1e24a | -1.33613 | -54.65598 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be070345-642a-310c-87e7-4b45f1418769 | -1.33047 | -54.24498 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4898b7ce-f46b-38b3-8c2e-650ff03e4ce6 | -1.32644 | -54.24834 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da149c7c-fe64-34bd-a74a-4416770cab4c | -1.32585 | -54.25214 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 856ae216-c870-3004-b9c6-87d2573bad9c | -1.32526 | -54.25591 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bb4489f-e1cb-33fb-867e-e2025b6df217 | -1.3231 | -54.20211 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38caae15-a7ae-3cc5-903e-aedca84203f3 | -1.28575 | -54.1969 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c23748d7-241c-3e97-860f-73143413ed63 | -1.28028 | -54.40979 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 334b21e8-4f31-3f72-98a3-e911fcbad901 | -1.27631 | -54.41288 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b46082a-ba24-3b8c-9a71-06cf66b50f0b | -1.26272 | -54.45544 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c41a1ec0-c619-3482-9f39-6206224cecea | -1.25932 | -54.45491 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f13a8da-e746-3d38-ae59-7571d15ee5a0 | -1.25875 | -54.45854 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f982cada-7732-3bd8-a086-f6483abe888b | -1.25535 | -54.45801 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 773e810c-7a6b-3b9d-b280-59eb27cdf959 | -1.25488 | -54.45827 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23765cc5-aac2-3bf0-8b03-4aced49bbbaa | -1.25205 | -54.45412 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 824674b5-3eca-3a2c-b838-b623b3204c24 | -1.25198 | -54.50224 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README68.md)
