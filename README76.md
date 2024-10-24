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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 029aa6b6-62ac-3f6e-b8a3-516505d82e94 | -7.59144 | -47.07942 | 2024-10-24 04:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3146ebbf-a9e9-3b59-9792-fa6daa9fdd68 | -7.59072 | -47.08454 | 2024-10-24 04:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b040760-822f-32f1-a6e2-ffc38e4fb4fa | -7.58138 | -47.54997 | 2024-10-24 04:57:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bceffc0b-5dcc-3902-bae1-3589ea87708b | -7.57682 | -47.54927 | 2024-10-24 04:57:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30ecf413-e44c-3265-b4c8-afda9d7a3bb2 | -7.51341 | -48.07871 | 2024-10-24 04:57:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a4ebd42-3817-34b1-a51c-d4f9c4ec4b72 | -7.50959 | -48.07384 | 2024-10-24 04:57:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a64c4db1-0e18-3128-b03d-c67ebdad8653 | -9.24058 | -48.31851 | 2024-10-24 04:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80cdfeaa-f3bb-3a76-af05-c1117a73a650 | -9.23998 | -48.32287 | 2024-10-24 04:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de8c16a3-e7a1-35b7-b2a7-6b252b3b67cd | -9.23674 | -48.31349 | 2024-10-24 04:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dd09586-51cb-3f2a-b803-9b6ba6ca1a2b | -9.2329 | -48.30849 | 2024-10-24 04:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92616e26-a412-3186-8090-141112c0a082 | -9.2323 | -48.31285 | 2024-10-24 04:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98dfad50-0672-3a5e-942d-d30c0f2d035e | -9.21176 | -47.95054 | 2024-10-24 04:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7918f367-0a60-3539-994a-20ab90c8d09d | -9.20722 | -47.94982 | 2024-10-24 04:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cbd9ff44-9364-38e9-8b11-df1c74bed082 | -9.20659 | -47.95438 | 2024-10-24 04:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 65c7c051-8230-371e-8cfb-26cd75fdcf4d | -9.20268 | -47.94914 | 2024-10-24 04:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f053ca88-8f8f-38ab-b144-5a5610c2220e | -9.20204 | -47.95375 | 2024-10-24 04:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 437b804a-f5d7-3b7e-bc9d-ab72e5f2b9f1 | -9.01979 | -47.75697 | 2024-10-24 04:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63fa4779-844d-31ca-9946-b4e3c54eb682 | -8.82191 | -47.93791 | 2024-10-24 04:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a6c8f3d-12b7-3fdb-b56c-146d73f066cf | -8.81738 | -47.9373 | 2024-10-24 04:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61ac7784-2b67-301a-8920-e7a227c4fe0a | -8.41542 | -47.98761 | 2024-10-24 04:57:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a69617b5-01c9-3a9b-8487-d460820c3b9f | -8.41094 | -47.9869 | 2024-10-24 04:57:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5471c9d6-78af-3cc6-bb03-e668ca8f42a2 | -10.89454 | -47.96338 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6fe1ff5-2677-3581-9228-484f9d3fa4b5 | -10.8884 | -47.90189 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 28f259d0-92c6-32c6-a4a1-4d1d36e0d04f | -10.88834 | -47.93848 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b6995da9-2c7b-38ad-aed4-061b8b33617b | -10.88767 | -47.90741 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e0ef59fb-8e46-355a-80c7-5247ba3cd5fa | -10.88302 | -47.90656 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2cd784be-58c4-39c3-8648-4119f021dc59 | -10.58929 | -48.02552 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 1dffb9dd-14f6-31e8-a84f-5fad1b6119c1 | -10.58859 | -48.03066 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8b8a563f-10c6-3961-8480-264e84a149d0 | -10.58465 | -48.02499 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b914732d-c023-3e8e-9e62-d9a0cfab7b8c | -10.58396 | -48.03012 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 424d684a-5f2a-35ca-b645-d95958b0ac35 | -10.41964 | -47.51801 | 2024-10-24 04:57:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ddb3c938-328d-301d-9a95-08750bd457d8 | -9.99254 | -47.99894 | 2024-10-24 04:57:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c958d235-b267-3ae3-b5ba-5e783ab1d880 | -9.92397 | -47.84763 | 2024-10-24 04:57:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf2b8013-623d-30cd-96a0-0b614013843e | -9.88906 | -47.80168 | 2024-10-24 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b9925fed-4fa3-3243-8d5f-0f6a2a870f6a | -9.8884 | -47.80642 | 2024-10-24 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5a88ff73-6ce4-31fc-b3b1-c77f11b8422e | -9.71433 | -47.65445 | 2024-10-24 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37283f48-d748-3af9-b5c1-541d117a3ab6 | -9.62671 | -47.91204 | 2024-10-24 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61548032-fcd8-33dc-abb3-f7af1cd95599 | -9.60948 | -47.60703 | 2024-10-24 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f01117e-a089-3fab-911c-c791fec1c0f4 | -9.60478 | -47.60647 | 2024-10-24 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a600f0ad-8e85-3780-ada2-eda55f750902 | -10.08569 | -47.72044 | 2024-10-24 04:57:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43832056-5e3c-3520-abf0-bd74575a2222 | -10.02455 | -47.45593 | 2024-10-24 04:57:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3ebf96b-d993-3b8a-a678-30ca6653547d | -10.01979 | -47.45522 | 2024-10-24 04:57:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e08590cc-f2c2-377a-83b7-48ff8fb0808a | -10.0191 | -47.46037 | 2024-10-24 04:57:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 69db0231-fd01-3e4a-9fd1-4a774a2e7b61 | -10.01504 | -47.45445 | 2024-10-24 04:57:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 336c0903-5338-3ad7-920e-2a5ecbdbd933 | -10.6426 | -48.55048 | 2024-10-24 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8d9d2f6-cbe0-388e-b219-c5ba67c8f145 | -10.48069 | -48.27998 | 2024-10-24 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7947faa-6056-3ccc-8094-02600a0208ed | -10.47944 | -48.28134 | 2024-10-24 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bb73b090-bdd8-3bd7-989b-61ec640e04b9 | -10.47489 | -48.28083 | 2024-10-24 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| db30c91b-1d2a-336f-b0d2-d0872fda5ff9 | -10.47034 | -48.2803 | 2024-10-24 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c13572e1-dbe2-3a37-938d-d291a3105c93 | -10.4697 | -48.28492 | 2024-10-24 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 174b827c-a248-3fea-a986-915de464ce72 | -10.45857 | -48.58477 | 2024-10-24 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b02de362-e630-30b6-8864-466168984037 | -10.45797 | -48.58924 | 2024-10-24 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4a55e46-bb58-33f5-b67e-87d34f7577cd | -10.32386 | -48.82113 | 2024-10-24 04:57:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39267bf1-be82-3298-b179-8f96e9045ece | -10.31952 | -48.82038 | 2024-10-24 04:57:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ade06918-bba9-3fb8-bdfc-3ceb44ef0e3d | -9.99376 | -48.85154 | 2024-10-24 04:57:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a3b8286-2deb-3c36-b41c-b24e7abc99d9 | -9.86836 | -48.56022 | 2024-10-24 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb20a5f6-5e0c-388d-946f-e2fc55385632 | -9.86777 | -48.5645 | 2024-10-24 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25a54651-f0c2-3ee4-8666-ef627a665d11 | -10.07654 | -48.85966 | 2024-10-24 04:57:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 626c2929-5053-3b3d-8695-b99609f77fcd | -10.69429 | -49.10923 | 2024-10-24 04:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fc8ca0a-b459-384c-98be-bbb4c6da53ee | -10.69194 | -49.10712 | 2024-10-24 04:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 957d9bfc-ddc0-3208-8ecd-1c6d0ac325d8 | -10.69139 | -49.11122 | 2024-10-24 04:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6d2f9e0-45c0-3806-a1ac-a67b3b2c02f3 | -10.68999 | -49.1086 | 2024-10-24 04:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e21ff002-cd54-3d98-a11f-0f8f9eff6af7 | -10.68942 | -49.11268 | 2024-10-24 04:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9b48fba-fe79-3d1b-8caa-b0cd126f477b | -10.6857 | -49.10796 | 2024-10-24 04:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9fbb860-4e5c-322a-b6c1-8cad676f16df | -10.68512 | -49.11204 | 2024-10-24 04:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32115bd2-4f5a-3b9b-b299-2aa94985fec9 | -11.14768 | -48.09431 | 2024-10-24 04:57:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bcdb9548-b81c-3798-b7ba-24135f4622a4 | -11.14613 | -48.09568 | 2024-10-24 04:57:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59d8e1e5-6694-3bd8-83ff-98b889ef2909 | -11.10413 | -47.70233 | 2024-10-24 04:57:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21ae6061-8531-315c-8fc4-ef150e799e24 | -11.10386 | -47.70352 | 2024-10-24 04:57:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d157ce72-04d3-3a0a-9e28-9b3eaa06af2e | -11.09937 | -47.70164 | 2024-10-24 04:57:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad608119-7f65-3737-abe0-b511108848a9 | -11.07774 | -47.9059 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 575d49d8-a799-3400-b056-263c936b62a4 | -11.0765 | -47.90429 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e711ee04-744d-367d-9f55-8433efbcd8ce | -11.07579 | -47.9095 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d47496e-dbfe-3148-beec-521c0b2c34e0 | -11.07306 | -47.90516 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c66c010-bb79-38ca-9de6-aba85e451220 | -10.97817 | -47.85241 | 2024-10-24 04:57:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 23bf0819-5469-3a4c-8b35-32cf7562ea98 | -10.97603 | -47.85429 | 2024-10-24 04:57:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d68869a-94f9-3a18-ac0a-b0925a643297 | -10.95473 | -47.83475 | 2024-10-24 04:57:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 981fccd4-062c-3833-8406-006bd63c491e | -10.93847 | -47.81307 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9d2c6b39-2f98-33df-a8aa-23a44d57282f | -10.93374 | -47.8125 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| eccd7a1a-6448-3f50-a871-c1808833ace6 | -10.93306 | -47.81758 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bfbf5fa9-ce54-39db-9a2e-1a99941314fb | -10.92906 | -47.81159 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b9251e0b-156f-3f04-9074-3e97cab904f2 | -10.92832 | -47.81717 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 88daa3ae-d0bb-32f1-a640-a6b2cb0cf1a6 | -10.92436 | -47.81085 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cfc6a13e-b77c-3823-b5f1-83362ffc3767 | -10.92361 | -47.81652 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ccc5f9bc-d36f-3ee2-9b5b-99e2d8989264 | -10.91175 | -47.97662 | 2024-10-24 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b01ecff-6379-3676-84ce-43ae20f49fa1 | -12.20711 | -48.06251 | 2024-10-24 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66a6429f-c242-3f56-bb39-884bafe7503d | -12.07711 | -47.98618 | 2024-10-24 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4bcf2c35-598f-3d8d-818c-31d6cd3a6360 | -12.07238 | -47.98551 | 2024-10-24 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37ae8bd6-c535-3d8c-bf41-4f8d92e6c759 | -11.7939 | -47.88427 | 2024-10-24 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16c17529-b6e8-31ab-8837-a998850e4dce | -11.79323 | -47.88936 | 2024-10-24 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1fe77581-e24b-3ebd-8128-a0a3538a0d8a | -11.78849 | -47.88866 | 2024-10-24 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e6af416-1e6a-31fd-8540-bf9dbc2efa11 | -11.72621 | -48.35662 | 2024-10-24 04:57:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fc4e9b2a-8540-39c5-b6f9-9553323b13f5 | -11.65735 | -48.80029 | 2024-10-24 04:57:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 83af8ba7-72d6-3f67-8fd0-cd2354aef0f7 | -11.65674 | -48.80478 | 2024-10-24 04:57:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 59d74ddd-b04f-3bb8-9fa8-490f025e3db1 | -11.64222 | -48.60545 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfc2ebd0-6efc-3deb-bfe6-fbf7f06b93af | -11.62027 | -48.38404 | 2024-10-24 04:57:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c8f45b8-113a-3d70-95a4-4aaf507ff7d4 | -11.61839 | -48.56849 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 710cda8d-7f9c-3a88-83dc-5c269213c421 | -11.60794 | -48.54374 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df722a9c-e57a-3877-9c14-0c986d14be9c | -11.60732 | -48.54832 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9bce5539-ace3-3403-83f7-92230a1f0316 | -11.60561 | -48.45839 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README77.md)
