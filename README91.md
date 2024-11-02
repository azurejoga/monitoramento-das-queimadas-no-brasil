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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8517551e-ad87-36f2-a6da-7e0b46394a44 | -2.45957 | -49.79029 | 2024-11-02 05:27:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 075d28e6-22c1-36e6-aab9-cdc2a4e210af | -2.43104 | -49.65581 | 2024-11-02 05:27:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 358824c3-71dd-330f-8efe-4d1b91ef634e | -2.42931 | -49.65152 | 2024-11-02 05:27:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d5b52fa-1bd5-3b5e-adfa-ea8fb3c11290 | -2.42858 | -49.65643 | 2024-11-02 05:27:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de7746c0-d96b-3a13-b9b3-22dad39c4a8a | -2.42478 | -49.65488 | 2024-11-02 05:27:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fab41bda-7fb9-3e7b-b552-838baff28ec1 | -2.38426 | -49.66876 | 2024-11-02 05:27:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41732542-3b08-3c4d-9d19-fee19bfe3aca | -2.37802 | -49.66779 | 2024-11-02 05:27:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e0a38e5b-7dc7-363c-b9e7-5d3e8ffb41e0 | -2.37728 | -49.67266 | 2024-11-02 05:27:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af063955-3fec-3689-a1b0-c32ffd72bfe7 | -3.2989 | -50.02157 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5d5bd19-e057-352b-bc7b-4a07c904511a | -3.29688 | -50.02229 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9d65b65-2640-39b6-b8fc-1e528df47eb8 | -3.29271 | -50.02068 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab16f38b-e1d0-322d-b608-3467c05bb72d | -3.29248 | -50.23087 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5486f837-ffc6-3d0b-bcfb-8950712059e9 | -3.29191 | -50.23203 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 748485f5-3d10-31b8-856e-7a9ed2983002 | -3.29173 | -50.23579 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 946011a7-0ce9-369c-b7dd-8be4b3708366 | -3.29069 | -50.02135 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da79c023-bf59-3172-840e-bca15588a8b6 | -3.28565 | -50.23469 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f8a7d3f-d2a4-36fd-8ce2-eed5aceda6db | -3.28512 | -50.23585 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18abf8bd-80bf-38dd-9a32-2a8a76b0cd8d | -3.27957 | -50.23362 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71f6ffe3-f09f-383b-83e1-d80734da7889 | -3.27902 | -50.23489 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 511e8434-6df7-360d-9f9f-af5509edbbbc | -3.2766 | -50.338 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea6d37fb-ec0e-38a0-912a-e22cd5c49db5 | -3.27642 | -50.33664 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22547274-45fc-390f-ab12-d0ef571e7c51 | -3.2712 | -50.33248 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a375edbb-2714-3d7b-b3fe-1ba929bf5833 | -3.27053 | -50.33712 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 706af1bb-7885-3bba-bdfa-6602ff58b8d6 | -3.27035 | -50.33575 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9fb867ae-c73e-30f1-9305-5806617fc0fb | -3.26987 | -50.34167 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fbb4fceb-3c5f-37fd-9541-2b68a76a3202 | -3.26966 | -50.34032 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 32210329-ba74-3629-be93-d6b66351f547 | -3.26921 | -50.34621 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7b838331-9466-3142-a366-301f74a63daf | -3.26897 | -50.34486 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 24fe31ec-f800-34f4-ae10-b4a3f183db6f | -3.26829 | -50.34936 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 29cd5914-dd82-356a-a362-a5930e7fb376 | -3.26447 | -50.33612 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84129bae-ebd6-3de7-82d0-76cc9d2431dc | -3.26429 | -50.33477 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0c78923d-51e8-37d3-bdcc-e9425c741cd8 | -3.26381 | -50.34071 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69793291-e845-31eb-802f-fdab361745ef | -3.2636 | -50.33937 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1a58ad2a-bbb6-30a1-bbe5-459c46ae62c2 | -3.26315 | -50.34528 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82be8379-1641-38ef-9fa7-6a74da639a7f | -3.26291 | -50.34394 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 86b7f148-e014-3988-8530-c68fdffe8cff | -3.2584 | -50.33521 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5e89183-cc46-3812-90f6-fff138897272 | -3.25753 | -50.33847 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76ac2d90-ba60-37b1-9a41-eea7c1b5387c | -3.25709 | -50.34434 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 788647d3-8a6a-351b-8781-9558aa62c257 | -3.25685 | -50.34303 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de4199dd-afd1-3a4d-9302-a8efb3517c48 | -3.25617 | -50.34755 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 889cac75-15ec-3722-a116-dae61059e069 | -3.25233 | -50.33434 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5729453-87a2-349c-a754-83b6dca87a84 | -3.25215 | -50.33306 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 586ea0ae-d40b-3a87-907e-cc13ad930f5f | -3.25147 | -50.33757 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 680f090e-bb11-302e-854f-662cffb0b75f | -3.25136 | -50.04368 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 705f67cd-b93b-30ff-b538-181f76c3fd46 | -3.25104 | -50.34338 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3460e751-b8ca-39cb-ad51-df9e9930bac4 | -3.25079 | -50.34208 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d051f8d6-408e-3c9f-bd47-7381ce3486f1 | -3.25068 | -50.04835 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c6d863a-3045-329e-8073-07837bbdb84e | -3.25039 | -50.34792 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65be9f8c-1da4-382a-900b-89dfe7e1cfd5 | -3.25011 | -50.3466 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 974f6544-951f-3f3b-a7c9-7cb406faeb77 | -3.24627 | -50.33339 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 374d551c-ae38-3dd8-879d-c8494536b703 | -3.24562 | -50.33791 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e53f57db-ffde-3211-88d9-5830649f07bb | -3.24541 | -50.33666 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd0a5359-5145-3695-b744-96fd378f31f6 | -3.18365 | -50.5858 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8d65bcf-bd54-3eb4-b9a5-edfc9d90a4a0 | -3.183 | -50.59016 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc4f44e1-3606-3bf9-a8f8-e09aa33d8707 | -3.17832 | -50.58062 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 216aafd1-e94f-3a67-bd5c-0d80a854e4b9 | -3.17768 | -50.58493 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f105ccf-29f3-3345-be7c-5d55cd0c2495 | -3.17704 | -50.58925 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14cfecf6-1e1e-397e-9ff5-2a30f52c9943 | -3.17235 | -50.57971 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc5843d5-c0b5-37d4-9708-d5cb4b8457a5 | -3.17172 | -50.58404 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b7bc4fa-a94c-34fa-9f8c-f7e27043e7c1 | -3.14386 | -50.35367 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0013f1d1-f6a0-378e-be57-31652750bcbb | -3.1427 | -50.35154 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35f2b0e1-3e66-3295-96f9-d65b09c5e96d | -3.14202 | -50.35609 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08600716-9104-3a4d-a777-926b6a6ded0e | -3.07356 | -50.23232 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e275ddb-9982-34eb-beb1-f754d53aca05 | -3.07325 | -50.23368 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ac8adeb-b247-3cd2-b0c5-982ae64ceefb | -3.07288 | -50.23679 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8de1494-17b3-3f6e-9cf6-35c945e1f3c9 | -3.07261 | -50.2381 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3183b11-abee-3cab-94ed-8862aefacb0a | -3.06747 | -50.23145 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25674209-89fd-3fe7-8b38-006f67146661 | -3.06716 | -50.23274 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c86c2bd-7117-3ad0-946a-f39a6ec82a80 | -3.0668 | -50.23584 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5aeee054-0afd-391d-85d9-737b81f97b1a | -3.06652 | -50.23719 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57ec60b2-9127-378d-a8da-a405e24a8bb0 | -3.06475 | -50.50325 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 175977a2-0368-3ad2-943e-7729c9a6beb0 | -3.0594 | -50.49804 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a657e5e0-b1a2-332a-868c-d95a2db144b0 | -3.05876 | -50.50238 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6dded8c1-13b1-3dbc-8b8e-aa91e9554000 | -3.05812 | -50.50674 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ea9e187c-1374-3002-8be9-5ad65257e17b | -3.05341 | -50.49714 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9042708e-a5ec-3a1d-87bf-0d6347c6df32 | -3.05277 | -50.50151 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0484754f-e143-39aa-8df5-322786746e13 | -2.57573 | -50.05425 | 2024-11-02 05:27:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb1925f2-24ad-3d3b-ab7b-156758faeb5d | -2.57505 | -50.05888 | 2024-11-02 05:27:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5dc4ed39-ffc5-387f-8b56-793895c1aabc | -2.4005 | -50.31248 | 2024-11-02 05:27:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 220c2b69-d253-3d15-8bff-793ff389aefd | -2.39986 | -50.31689 | 2024-11-02 05:27:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3870139a-f5f1-3585-848f-b54c618a6aa9 | -2.39885 | -50.31303 | 2024-11-02 05:27:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42c1974b-b5ed-36a2-ac3c-633fbbe5c826 | -2.39818 | -50.31744 | 2024-11-02 05:27:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f56b982-260f-33de-977a-9af835c624b7 | -2.19805 | -50.31522 | 2024-11-02 05:27:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| facf74de-39b0-390c-9839-c5c05fb999c0 | -2.19207 | -50.31435 | 2024-11-02 05:27:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a723521a-a865-314a-9577-a569b7ef92f1 | -4.80699 | -49.48479 | 2024-11-02 05:27:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7efa04b4-280f-3ac4-8398-b57b984c74fe | -4.80044 | -49.48398 | 2024-11-02 05:27:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fca052c7-bdbd-3662-84da-aeee48b68948 | -4.71067 | -49.60335 | 2024-11-02 05:27:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| c403e3e4-dc5c-3ebd-aa59-aef154981bb6 | -4.70989 | -49.60884 | 2024-11-02 05:27:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| d978a714-0fdb-3992-a5b6-77c7e77dd51c | -4.14913 | -50.74762 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3047637b-8096-3f20-8a6a-981740f70ca5 | -4.14854 | -50.7518 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d91aadbd-2265-35cf-84f1-054b6e8d0ae7 | -4.09702 | -50.7514 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a7ceeb4-5b85-32a0-8270-f0dcbef36b97 | -4.0964 | -50.75571 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2400ed2a-64ce-3cc4-b1a0-0fec5995b3e1 | -3.70841 | -50.54433 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82f3f96d-f2f2-3d12-9faa-c7f04615e047 | -3.70777 | -50.5487 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 130a61f2-da54-38cc-9a3a-efaf1a02c96f | -3.70329 | -50.15749 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17f6d618-6dc0-3a42-8733-53a3ac1c58fc | -3.70214 | -50.1538 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5f02dda0-77c4-3c2a-94e5-f4cea384956b | -3.69849 | -50.1473 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a4e23cb0-0e15-3c5b-ac18-51e6546141a5 | -3.69779 | -50.15208 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4f3f5655-810b-3b24-828c-cce5773016e6 | -3.69662 | -50.14815 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b7cb7d6-f556-3c03-b284-458361a3b4e6 | -3.69594 | -50.15299 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README92.md)
