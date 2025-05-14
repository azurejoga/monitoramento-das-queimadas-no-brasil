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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11222fd6-dbff-34ba-8c70-10b724aa526e | -12.99859 | -48.88023 | 2025-05-14 04:46:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b77b0c71-009a-305c-a055-17d6a62890d2 | -12.49798 | -57.21367 | 2025-05-14 04:46:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 475aff9f-f110-3255-b4de-b5d7d2004086 | -12.50191 | -57.21435 | 2025-05-14 04:46:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e074c15a-0300-368a-8202-8e3b53852d5e | -12.72947 | -54.97 | 2025-05-14 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e5ce764-0f39-3a30-af1f-54ba6918cc90 | -12.87052 | -55.05824 | 2025-05-14 04:46:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 443c3859-b82b-3e9b-90fa-7e423847e44a | -11.25807 | -52.47583 | 2025-05-14 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d56db18-a049-3208-ac99-92e98a4c47e1 | -11.13404 | -54.22188 | 2025-05-14 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3ff0389-7165-3765-b873-653f9a0076a2 | -13.55914 | -52.87799 | 2025-05-14 04:46:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 949ce712-6c11-301c-af60-2607b1b5d4ca | -11.79279 | -47.37542 | 2025-05-14 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b7dc3ee2-86a9-3ba8-a8ef-46552d2324f1 | -12.08876 | -54.57536 | 2025-05-14 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a40c0f8-968a-34d1-bcfa-d2f21aba11e8 | -11.8026 | -46.64462 | 2025-05-14 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c8b05c4-efe6-33dc-8d4d-5674dcbbe6c9 | -10.13558 | -47.10762 | 2025-05-14 04:46:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9e88046-c386-3cf0-a59c-33355e04780b | -8.80238 | -49.81653 | 2025-05-14 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 725ecdfc-72d1-373b-8ea9-efb2f1c37378 | -11.63085 | -48.126 | 2025-05-14 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 340fe5c8-b00a-3ad3-aa3e-4c42b4ea58ca | -10.66175 | -44.49173 | 2025-05-14 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33e907ae-aec9-33e0-b3b0-b3845edb488e | -10.24456 | -47.60073 | 2025-05-14 04:46:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29eb30fa-c790-31a2-bac6-90babbf98d19 | -13.56629 | -52.87555 | 2025-05-14 04:46:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20bf2e2f-8676-3830-8659-0045a05ec0bd | -10.45624 | -49.07864 | 2025-05-14 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59f44201-8f0a-35ce-9e6f-05101e85841c | -12.35239 | -44.81665 | 2025-05-14 04:46:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3a57934-952b-33cf-b369-e6f019f5b446 | -12.35133 | -44.81582 | 2025-05-14 04:46:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b84cf55-252f-39dc-912c-3c820e146196 | -9.26802 | -50.2158 | 2025-05-14 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 712686ad-d440-3ded-a16d-65d8655d06fb | -10.63415 | -46.27915 | 2025-05-14 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0085da2-8b0e-3dc4-afb8-5f4538b66945 | -11.79152 | -47.37643 | 2025-05-14 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b2d36a99-948b-3aba-8ace-4ed811ed3bc7 | -11.43652 | -54.09269 | 2025-05-14 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ab5ed18-1d54-3008-9257-9e336a4142aa | -13.55858 | -52.88152 | 2025-05-14 04:46:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a388d676-fba4-3178-a8be-0d8d0b5116ff | -11.66004 | -54.95381 | 2025-05-14 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc37d54f-1df1-3e55-ae92-e974a61c5bb8 | -9.99723 | -47.84007 | 2025-05-14 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e332362-ead4-3609-b06a-65c5f79bdd84 | -12.2927 | -52.47191 | 2025-05-14 04:46:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dfce2b5b-63c7-330c-9f3d-4e46148807c9 | -11.69262 | -48.81946 | 2025-05-14 04:46:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e683911-873d-30f4-89d6-b2bbe4a96f9a | -8.7162 | -50.24541 | 2025-05-14 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7151adaa-acc5-3343-970c-cae137ad8934 | -13.60454 | -47.38363 | 2025-05-14 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b197bb6c-5f2b-3263-8bab-d3020eabc9c7 | -13.06343 | -52.02312 | 2025-05-14 04:46:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37ed893b-0aa9-3275-87b2-a5d9180bce6f | -11.42093 | -46.983 | 2025-05-14 04:46:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 979459f6-ec1e-330e-af22-e0742d786728 | -11.37405 | -55.12043 | 2025-05-14 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea624ed8-bc56-3f70-b3e9-555774ac7871 | -12.68616 | -58.12669 | 2025-05-14 04:46:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b710559-a582-33e6-b52a-6689b7d1ace7 | -8.80294 | -49.81285 | 2025-05-14 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ee07bb63-4071-3dbc-8ae9-1422b635fe32 | -10.48235 | -49.14704 | 2025-05-14 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6739a6b1-df53-3325-b1a6-d08a4f5c3d9d | -9.99658 | -47.84472 | 2025-05-14 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed56e6ea-5739-33fa-8b25-829d911a630f | -13.04774 | -43.48819 | 2025-05-14 04:46:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c03c3967-1c42-3b66-93ce-8e83fcf806ad | -13.06084 | -52.01567 | 2025-05-14 04:46:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ac05d6c-337f-32c2-aa01-8fbf43c45334 | -13.08002 | -52.04753 | 2025-05-14 04:46:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d1470e2-a9d6-331e-8448-6225e56c4820 | -12.64756 | -54.0828 | 2025-05-14 04:46:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9123f7d-becc-35c5-a249-00f0a42e9605 | -11.55489 | -47.61523 | 2025-05-14 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06b1e85f-d4a3-3552-918b-f23af5301b39 | -11.8496 | -57.85744 | 2025-05-14 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84624ef4-77c0-345b-aafc-113feafa120a | -9.4718 | -40.3172 | 2025-05-14 04:46:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 181199f0-a67f-3eaa-b3f1-da7fd4ba7a51 | -11.50562 | -48.58734 | 2025-05-14 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2c4a349-c851-37bc-ba5b-6ca7995160d5 | -13.675 | -53.94535 | 2025-05-14 04:46:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac6bea0f-2895-3775-bea8-1a733d929f68 | -12.50496 | -57.22015 | 2025-05-14 04:46:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db552476-9ed3-39b2-890f-702ddb7094a6 | -13.05382 | -53.72261 | 2025-05-14 04:46:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9956e0dd-85ef-3d51-9222-09047c4e76bb | -13.09354 | -52.28843 | 2025-05-14 04:46:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7848c86a-f43c-3d4f-9fab-685e013d8f19 | -11.20574 | -49.16898 | 2025-05-14 04:46:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 835f4706-54f2-36e4-a0f3-ba5fb75c98f5 | -11.57389 | -47.44728 | 2025-05-14 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b68cdb7-d0e3-3275-86e8-4ac3276aa4a0 | -13.05106 | -53.71843 | 2025-05-14 04:46:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf84ef53-55e9-36b8-822c-35d6e8d37dfa | -12.50103 | -57.21947 | 2025-05-14 04:46:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4124e63a-4e61-3614-810e-7ac706abf48e | -13.59956 | -47.38976 | 2025-05-14 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3adbc541-41c7-308c-94fe-f385b86ed6ba | -15.27545 | -43.07624 | 2025-05-14 04:46:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 6a9abd92-3fd4-3d74-80f6-d94dbf8ddadf | -14.41438 | -49.77906 | 2025-05-14 04:46:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 191c7911-4dbd-3a25-8a6b-0f20e27d4303 | -12.34918 | -49.95794 | 2025-05-14 04:46:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eea77b60-10aa-36e3-a9ed-41785ae4f99c | -8.71565 | -50.24899 | 2025-05-14 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7dea24b-8113-311a-9e58-0fe30ce37999 | -10.18228 | -48.02507 | 2025-05-14 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24158637-aa6c-3b8d-9517-2be0ee97cb7b | -10.00099 | -47.84068 | 2025-05-14 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc30ff83-634e-327e-a4af-314e9a4a6ef3 | -11.57023 | -47.87272 | 2025-05-14 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92f3d768-cba3-32e5-83b1-0d0b9e6bc12b | -12.68964 | -58.13126 | 2025-05-14 04:46:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ccd99a72-ac28-378c-bc45-908de44771f8 | -10.00475 | -47.84127 | 2025-05-14 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e052891-c013-38cd-acb5-8b4e1212e527 | -11.65937 | -54.95785 | 2025-05-14 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb274296-71dd-3588-9a0f-3035edd9f2cf | -13.16324 | -53.2737 | 2025-05-14 04:46:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d4273e1-64bc-3501-83e5-34316357a136 | -9.57514 | -49.11269 | 2025-05-14 04:46:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83ecbb50-a759-3658-8b74-ca599783363b | -11.79427 | -47.36502 | 2025-05-14 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 23707b2f-d4dd-38cc-bab7-f927e320d67e | -13.56188 | -52.88206 | 2025-05-14 04:46:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba06e22e-e6c5-3717-b379-e9daa9ca5795 | -11.85026 | -57.85361 | 2025-05-14 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d94d2d6-67a7-30e5-b837-ae00aa820682 | -11.56639 | -47.87217 | 2025-05-14 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 293ba690-0c55-30eb-a217-5accb6d84551 | -11.69567 | -48.82119 | 2025-05-14 04:46:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4b1887b-89a9-3ffe-ae93-e0ff6b5bf88f | -11.39931 | -48.70133 | 2025-05-14 04:46:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f34a237-397d-39af-9aeb-9422a43994d3 | -12.50978 | -57.21572 | 2025-05-14 04:46:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cfa7b6f2-dd88-3a37-9a9e-a859e9ad7eec | -11.79353 | -47.37024 | 2025-05-14 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8b3db4cd-e5d3-381a-a5c4-14734c539b74 | -8.30729 | -48.05589 | 2025-05-14 04:46:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a0088ce-3d40-3162-8e5d-23c1b786383e | -9.57574 | -49.10874 | 2025-05-14 04:46:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7e51743-d558-3bf5-b597-7522a9466c3a | -13.07671 | -52.04699 | 2025-05-14 04:46:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63818320-6aac-39bc-b551-1477801462b0 | -13.04321 | -53.72453 | 2025-05-14 04:46:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42335136-6b82-32a2-812c-f96972a030af | -13.56244 | -52.87854 | 2025-05-14 04:46:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a6cd9fb-0603-35a1-bb12-a25991297481 | -11.16648 | -48.68056 | 2025-05-14 04:46:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b905c639-b119-3f34-8624-fdd5a73cc7c6 | -11.9162 | -54.40556 | 2025-05-14 04:46:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3bb5ea6f-b117-32aa-91b7-588cf7bee701 | -13.39179 | -47.50916 | 2025-05-14 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88a04d63-3b3f-324e-9c84-b5862976ff15 | -14.63224 | -45.10085 | 2025-05-14 04:46:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 677af3d2-3017-3182-9215-d68b86c75dbd | -10.00787 | -47.84645 | 2025-05-14 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b23e719-98f4-3e0f-a104-cb15eac5d644 | -13.68714 | -47.77406 | 2025-05-14 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d0611de2-e1ba-3571-a24c-ab8ccd5111dd | -13.0499 | -53.72565 | 2025-05-14 04:46:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab33d2e2-8ed0-3f37-8438-2449df7f5acd | -15.26989 | -43.07563 | 2025-05-14 04:46:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 20.7 |
| c5ba147a-7b33-3f6c-b287-1782eea66ca9 | -9.99612 | -47.84275 | 2025-05-14 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e7af2984-64e4-3006-947d-0a56bc0833ea | -9.25766 | -56.32799 | 2025-05-14 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e67de113-f437-3557-999a-03220f2c2b0c | -13.39227 | -47.50573 | 2025-05-14 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5504f2cc-1f77-3d77-ad29-24f533f7d224 | -14.63291 | -45.09545 | 2025-05-14 04:46:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a03d64c-997e-3751-bb2b-1d17a86c9627 | -13.05048 | -53.72204 | 2025-05-14 04:46:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e8bdded-bf5d-3cab-8b3a-4b3425da2e96 | -11.63077 | -48.47227 | 2025-05-14 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9ed7161-d34f-35c9-aa7d-554d5087b4ea | -9.39918 | -51.02205 | 2025-05-14 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cc7072f-5311-3b66-a43f-1bdbd5f5e3e4 | -13.6905 | -47.77041 | 2025-05-14 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5914679-225a-3d19-b6cc-b7abae362129 | -11.40599 | -48.70679 | 2025-05-14 04:46:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56812417-230d-39e8-951b-3ed81b20e431 | -11.79619 | -47.37185 | 2025-05-14 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65afe680-4a42-3c96-a669-a5eb8d29abe9 | -13.07114 | -52.01711 | 2025-05-14 04:46:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8be5d14-5ac6-3aca-a00f-d7d1ea9dd195 | -12.64696 | -54.08649 | 2025-05-14 04:46:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README8.md)
