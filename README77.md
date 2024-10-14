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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3916219-0d54-3901-9d6a-8826f3d099f8 | -4.17805 | -46.73957 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da4a40e7-d5da-3f9b-9fe7-00cbbbe60a16 | -4.1513 | -46.86595 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b2cea7a9-c932-3dfb-8139-8f0fc2fbf6ea | -4.14827 | -46.86099 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15af3059-b904-3ec0-aa0f-c4d00b5876bd | -4.1476 | -46.86545 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb431744-d325-311e-b02b-37422a38e7a5 | -4.05953 | -46.22686 | 2024-10-14 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a865cbb-bd2f-3129-81b6-ad5126d313b9 | -3.94588 | -46.44007 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 6cde8cc1-d3a5-3da3-a085-a76fb407dda3 | -3.9421 | -46.4395 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 300c3d18-3b9f-30ea-bdd6-00283c8e2061 | -3.93595 | -46.42922 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9a6fbba6-a054-3b4f-9f4e-7bd61de22c99 | -3.93219 | -46.42857 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cd48f917-93fe-3ff4-b349-9cd85aa2689f | -3.93054 | -46.41406 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8bf4c4a-a755-31dd-bc6c-e0a0eeef3046 | -3.92677 | -46.41345 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ebf19ae-0b86-300e-b2a7-4ed1552c28a0 | -3.89781 | -46.45132 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eed3d205-2bb0-39a0-b076-13ea98f5f740 | -3.89711 | -46.45594 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7c2cda7-e2a5-3b51-89a0-eb803aa8c2c3 | -3.88956 | -46.45483 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb844b62-9b9a-3054-b638-a77732549574 | -3.87932 | -46.47158 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80838a3c-84fc-343a-909d-380dc146f38e | -3.87757 | -46.45766 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 130c10b5-a9fc-3489-836b-80bbb3250837 | -3.87622 | -46.46663 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac72925b-d9bb-3acf-bfd9-6bf76b0a149b | -3.87555 | -46.47103 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca4a240f-9120-3ceb-b28a-60c218ad9dd9 | -3.87245 | -46.46607 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20cc09b9-94e2-3217-9691-77993c8753e1 | -3.85682 | -46.91845 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7986817-077f-3671-95d4-c4dad29abfa8 | -3.85651 | -46.47065 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08a9abbf-71cf-3eb1-bc29-c30ef54e4680 | -3.85604 | -46.47269 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa74232f-b2f1-331a-a3a4-947b10c2dd71 | -3.85379 | -46.91375 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2ce2501-158a-37af-a2f5-2aa49d1bf5e9 | -3.85314 | -46.91796 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a26a7e4b-bc99-3d79-8339-c63525da6b10 | -3.85249 | -46.92217 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b5b4bb9-634b-3115-b5af-e35c0da6eb0e | -3.85227 | -46.47216 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 982fcf30-250a-3533-a28b-8a850f226001 | -3.85205 | -46.47451 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c87e1b4-ceb6-3a55-8a20-677b7c50c1d2 | -3.85077 | -46.90892 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5ee4284-5f26-334b-b69f-d2534610886b | -3.84946 | -46.91744 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa7fedf7-a43f-3616-9d5b-a6d89228159a | -3.84881 | -46.92166 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c8261a3-8858-3033-9981-80e8bcb0e0cc | -3.84776 | -46.90406 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a37efac-da0c-3c0c-ad55-b3d21e6ed108 | -3.84579 | -46.9169 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7acbc799-863a-320e-ad36-50d01f618aca | -3.84513 | -46.92114 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46641f5f-4b2e-3e5a-b270-a60d4fd9019c | -3.8445 | -46.47349 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 949fa6d8-2251-30b6-9aef-f8f315e98d16 | -3.84409 | -46.90347 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c26e4f5-fc8b-3d48-84e6-6f5efeeb959b | -3.84382 | -46.47788 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb4850be-f8b4-3cd6-a559-66fca6ffad7d | -3.84343 | -46.90779 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aae80484-c4d0-34cc-98e9-87b98779646c | -3.84276 | -46.9121 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c77b86d-3c30-31cd-8d0d-4562538933e8 | -3.84211 | -46.91636 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b51c8f62-eda4-3199-af1b-833786f3355d | -3.84075 | -46.47286 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f9af574-5c49-3f96-9126-4f78dc79d734 | -3.84042 | -46.90284 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5926a9a8-5fb5-3e22-9d8c-1e9ef9075588 | -3.84007 | -46.47724 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77eb3146-2caa-3917-9133-6f106e0bed3b | -3.83976 | -46.90718 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72cc7cf0-fa6b-311e-8290-14c541ff51ff | -3.83937 | -46.48174 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f04b082-7c8c-36f2-9b0c-f8a6994b538a | -3.83631 | -46.47665 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 18d49328-e5ea-3f05-8faf-6096fc3566d5 | -3.83609 | -46.90657 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04d8d12d-34a9-37f8-9fb3-925e47fdada4 | -3.83562 | -46.48114 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0cdc93d-36f0-301d-8594-aa320985459a | -5.65074 | -47.9214 | 2024-10-14 04:44:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 81a49e53-eef7-37f1-9c8e-7ddd5e1f9c04 | -5.65012 | -47.92541 | 2024-10-14 04:44:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5fcd2dda-845a-31fb-bb32-1f1530bbb527 | -5.64656 | -47.92485 | 2024-10-14 04:44:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a679990b-0792-38fb-9288-4b6935d0b33a | -5.52727 | -47.11728 | 2024-10-14 04:44:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66bd4ac1-2703-395a-a680-3439cddc0860 | -5.5242 | -47.11245 | 2024-10-14 04:44:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fd84c07-ab62-34a0-928a-0b1290a32e7b | -5.52355 | -47.11679 | 2024-10-14 04:44:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8757ef2-ad8b-3873-aa30-accf8d5671b7 | -5.41523 | -47.92914 | 2024-10-14 04:44:00 | NPP-375D | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 951e79d8-c4bd-3ddc-bb9c-cde0920de755 | -5.41168 | -47.9286 | 2024-10-14 04:44:00 | NPP-375D | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3cb4f8e-1965-38f1-90cc-9a950b8618aa | -5.41107 | -47.93258 | 2024-10-14 04:44:00 | NPP-375D | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4700a366-57ad-3f4f-9afe-9879f686fb1a | -5.40028 | -46.6558 | 2024-10-14 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd19b3cf-e27c-3aab-ac2c-343950f1c50b | -5.34357 | -46.60242 | 2024-10-14 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42e95d6b-6d7f-3725-a308-59f4137491f0 | -5.14562 | -47.59781 | 2024-10-14 04:44:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32531a77-8093-349f-9489-b3f0b873998b | -5.145 | -47.60189 | 2024-10-14 04:44:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c58e309-f52e-3861-a91e-05818a00c9f2 | -5.14202 | -47.59727 | 2024-10-14 04:44:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c50a542b-3cb9-3b94-952c-e2e56516be44 | -5.13381 | -47.35757 | 2024-10-14 04:44:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47521d52-b9ed-3e14-b545-d6c33c13b510 | -5.13079 | -47.35283 | 2024-10-14 04:44:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 57165089-b425-3695-bbfc-644ce628220d | -5.13017 | -47.35699 | 2024-10-14 04:44:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c513b920-6d2c-37a5-bae9-df4cbb1defa6 | -5.1259 | -47.36062 | 2024-10-14 04:44:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 78b436ba-331f-377c-94c5-961bc7393dee | -5.08551 | -47.60595 | 2024-10-14 04:44:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 509562e9-ba12-3eef-8780-6339f50d23c2 | -5.08368 | -47.60706 | 2024-10-14 04:44:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d96235d-7350-37ea-a469-5938c2458e53 | -5.08191 | -47.60545 | 2024-10-14 04:44:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3277d13-cd47-3214-b732-eb14a0cb4870 | -6.18412 | -46.95118 | 2024-10-14 04:44:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ae33cf9-ede6-3c47-91ac-c2de9546e988 | -5.53617 | -46.90488 | 2024-10-14 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84d11c76-217b-3701-bab4-2b6180b1892a | -6.04537 | -47.13508 | 2024-10-14 04:44:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e206cdb7-cbfd-3bec-9f66-31076d718e05 | -6.04471 | -47.13953 | 2024-10-14 04:44:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48e4d313-e495-3ced-85df-abf161179780 | -5.92288 | -47.74828 | 2024-10-14 04:44:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fda5524-d070-3079-9977-40cf9d7c3aae | -5.86042 | -47.62422 | 2024-10-14 04:44:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95d31c62-c0cf-3d3d-9d23-744c89b6b2e8 | -7.2552 | -46.96977 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f003949a-4f2e-3f83-a11e-1c94bddcb288 | -8.01283 | -47.21312 | 2024-10-14 04:44:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec725807-ec89-3478-a412-8dd1db2f1e80 | -7.67288 | -47.32376 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38bc8039-c879-3bb6-b69f-87d08d47ccbe | -7.67047 | -47.31408 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cdeb5bc-6b57-3ce0-91fe-3b1d569b1611 | -7.66912 | -47.32319 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f3c3bcd-007f-35df-b73a-e2e8a2c78199 | -7.34499 | -47.27781 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4008e80b-3602-386e-94c4-e43a5b57b0c7 | -7.34122 | -47.27729 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 106e8c30-f9ac-3761-901b-4859aa7348a3 | -7.33745 | -47.27677 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e64bf66-38d8-3388-9b1f-36a4f9cb6e64 | -7.25901 | -46.97043 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1d5eb8d-ef74-3b99-8ad6-07c71004f6be | -7.10422 | -48.33178 | 2024-10-14 04:44:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7deddc8f-b309-342f-a9b4-e1f243cc3e7a | -7.02348 | -48.32077 | 2024-10-14 04:44:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b84b11b8-5595-37a8-94ab-f99656967c64 | -6.98341 | -47.32642 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28532789-3b0c-33e2-886a-7f8f478a572f | -6.9476 | -47.49221 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0de7363-c9a3-3205-8587-4c087c37870c | -6.94391 | -47.49159 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 31129140-221f-3344-92b7-65153b8d7262 | -6.94251 | -47.48896 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e6073b1b-064f-3f8c-8d89-d6cb506a6644 | -6.94185 | -47.49327 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5db59ea9-4e75-3a16-a5fa-70f54362ef13 | -6.94022 | -47.49099 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b3f96a97-2c94-3008-a311-3a6c8d7ca62b | -6.93882 | -47.48836 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d6e4edb6-e8bb-3c57-a494-a0eca848cd0f | -6.93716 | -47.48607 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 037f819f-e4e4-3862-a60a-50b7b86323d2 | -6.93652 | -47.4904 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ca7c26f-d5ab-3467-a3fb-337e601fc30c | -6.93578 | -47.48346 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0d98636f-ec62-3eb4-b33d-84363c0c6ecc | -6.9341 | -47.48115 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1da26f4a-a850-3c97-9255-2f8ca627c80e | -6.93346 | -47.4855 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 119f681b-cf4c-3eb2-b28b-4012d8c723a2 | -6.93275 | -47.47853 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| caf16b0e-59d2-3316-858f-b1c7f187d1f2 | -6.93209 | -47.48288 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d1112923-d7a3-32dd-9bc8-2fb3b1709616 | -6.92906 | -47.47794 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README78.md)
