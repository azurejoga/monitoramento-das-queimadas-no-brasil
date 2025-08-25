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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec77a151-b18c-3227-b349-1bfaf81b0ba2 | -12.76291 | -48.11163 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8feff78c-45f7-309f-9bea-1f9c5394df4c | -9.197 | -59.48663 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6274f324-35ec-3b28-885a-8f664651d19a | -9.17498 | -60.77102 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58ad1461-68ef-32a4-8c88-2ec23ccc3ed3 | -13.43067 | -46.91863 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a4489e0-1a2f-3b2e-ae69-d70860a34c1d | -11.16953 | -55.03033 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2ff97fd-b4f1-3bd7-aa07-cfed5b09a8ca | -8.54418 | -48.86253 | 2025-08-25 04:42:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f7b81ac-bc1d-330f-998e-829deb9e6bd8 | -10.24958 | -59.10508 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 696384f5-6970-3e8b-9ed6-eab8c1215450 | -13.44572 | -46.91874 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a07dff1-927a-357c-be90-cca658bd2af5 | -13.43758 | -46.92435 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a33ba648-dd0a-3f12-be78-236adc830f86 | -9.19913 | -59.50519 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2ca67aab-6f34-3fd3-bf57-67ebfbabdc4c | -9.2121 | -59.70851 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ebb2d24-5667-31a7-b8df-4e14b3d17199 | -6.79391 | -58.63922 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af0e0eb1-7def-3b92-b032-ac726cdd8c85 | -13.46429 | -47.00673 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ceda08ae-9dab-311b-9707-4ddf8de64f34 | -8.22011 | -61.39527 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0ef53792-a4cf-3bd2-bb47-6bd23ef550d9 | -13.46878 | -47.0022 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 39c9cb4e-d1a9-3ddb-b4fa-9b8fc23bfa24 | -9.17417 | -60.77534 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b375a07-348a-38a0-8cf7-be9b32474ec2 | -13.62268 | -48.15714 | 2025-08-25 04:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21c0bf30-6807-3780-82d6-0bb81b050b22 | -9.1844 | -60.78623 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| bf88a14c-5135-309d-ba20-751819fc3ef6 | -13.43538 | -47.02095 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 190ddd41-4357-3938-9558-cfd55fab7177 | -11.61525 | -46.24509 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07ee7a25-f9e2-3e9b-baab-f371882d2a56 | -13.39298 | -51.80988 | 2025-08-25 04:42:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1ed7b18a-fceb-3272-a19f-e5203b605a13 | -8.0678 | -49.68152 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e91cdd4-cc45-3fcc-99bb-6fd639a5916d | -11.19834 | -48.47112 | 2025-08-25 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56d62595-7632-3016-a6ff-3c205b4c4712 | -10.89136 | -55.79488 | 2025-08-25 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 825a15c1-6810-3dda-bb14-7797bcc3ba7e | -8.10621 | -62.86679 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b68b3e8c-3d24-3334-ad06-64f733949f5d | -11.60702 | -46.23537 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1250fd5c-0d33-3a4b-9dee-8a7ca2b59f76 | -10.61145 | -55.05698 | 2025-08-25 04:42:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2b89849e-8bec-3c66-a793-abbf39cbd893 | -9.19903 | -59.43975 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 182d91e0-9e24-3aa3-b1f8-7897be6ad407 | -13.45013 | -46.91479 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffc0eaeb-f899-3b6e-8ea6-d3cface03738 | -13.6322 | -48.16672 | 2025-08-25 04:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9cfb84f-c8bf-34d5-a066-a3e7d387d0b8 | -13.28525 | -47.50799 | 2025-08-25 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff1ddc4f-0bf2-3561-b2a0-1cfac0e4d362 | -10.03562 | -59.35815 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1738dd15-3255-3df5-9bf1-67a3c42c1b76 | -12.93917 | -46.31722 | 2025-08-25 04:42:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd653fb2-cac5-3c7f-af1f-b7811a35bdba | -9.51992 | -60.51801 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 349e24e6-f27a-3b03-af6c-55fc6e8a27af | -8.09993 | -62.86669 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 755af8cd-16f2-3454-b94c-bb2d9042422e | -9.19807 | -59.47593 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fae26f59-f97e-38e5-bc85-af09451799a4 | -6.82758 | -58.95407 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fbbeccaa-78b5-3760-8522-b4d844c67f90 | -13.50928 | -46.90693 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f711db6-9cc7-3d2f-a712-b84db7bc6525 | -9.51876 | -60.55623 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56b62984-efa7-3ea6-9a34-d5f142d11fbb | -9.26302 | -59.7737 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| acb1990a-d061-3024-a330-522af59d398b | -8.60837 | -62.65057 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cfc4f23-3dfd-3a34-92de-11ad79b45c1e | -9.14938 | -59.49586 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b00bd99-eea1-3bca-a7b7-5d3cce2e1f9f | -13.40767 | -51.78282 | 2025-08-25 04:42:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73834e74-a22a-304d-89a6-7f5449e33dc3 | -8.86069 | -52.0502 | 2025-08-25 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f8e4edab-2c02-3ca6-bd60-08a7e45901b3 | -8.22292 | -61.38052 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 776658d1-86e0-3228-854d-143e85ee2326 | -10.88855 | -55.78658 | 2025-08-25 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c490d5c9-6b93-3a21-b3eb-d7be3634ce86 | -8.91819 | -62.41882 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf0dd922-5ef6-35fc-9a37-542ac6f0c030 | -9.18882 | -59.47036 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4cff9db-347e-3a33-aea5-a0abadb8b5ff | -11.63723 | -46.22857 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8153beaf-5170-3b98-8f3a-b38a64df4fda | -8.32004 | -47.26454 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5782f094-e347-38f4-9ced-fd37180aea28 | -12.49778 | -53.82656 | 2025-08-25 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f679a5e6-371e-34ab-915a-1505e506e931 | -11.28542 | -44.98668 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 878ea639-af43-3287-9639-c21f14f43c77 | -10.819 | -46.38768 | 2025-08-25 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 604401a4-8bf3-3e94-b51e-1bf1cd1d168c | -8.91711 | -62.42439 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0ef04578-e759-3e0e-947e-f370a60a4f24 | -13.43424 | -47.02902 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9fa875bc-f11c-39fa-b116-0481520da3ec | -10.61234 | -55.0518 | 2025-08-25 04:42:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2fba0350-c9ac-3fbe-9171-34990f114af1 | -6.6283 | -58.54895 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 913c29e3-02e3-326a-8540-f9c2b6d90cf5 | -8.90395 | -62.45712 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ecc08ff4-458e-39ca-a2fb-e2b687489e41 | -13.46255 | -46.88098 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4209b8d-0a1e-3ab8-9f6d-9e12978811f8 | -11.69931 | -60.18504 | 2025-08-25 04:42:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb617b66-3159-3023-ad4b-4a2bfad3988a | -8.0595 | -49.69091 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| d5a74f0c-858d-3338-8749-d3b71f3eeb08 | -9.15353 | -59.50388 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5c6b079-c8a7-34b6-9680-36d72dce70b4 | -8.22204 | -47.17383 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| adb0639c-8105-3a18-ae2c-75832e33068e | -8.10431 | -62.88031 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0811d90d-a5d7-3658-bced-efb80185547a | -13.44707 | -46.91215 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc6d0809-d37e-3c1f-9b57-87257cffd3e0 | -8.2332 | -61.42842 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c20bbf4-0a1d-372a-b75c-a06c05a3e8f9 | -11.17039 | -55.02528 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bcfe36ff-2ee0-3446-8904-5bb878a9f279 | -9.16905 | -60.81983 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93dec249-2105-3cf1-b605-400430b4a32e | -13.45494 | -46.87994 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20188154-cd1d-3ac3-bb67-b5be80735308 | -11.62816 | -46.23708 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4d630b27-471d-3266-96e0-936b7e4653f1 | -11.1949 | -48.47058 | 2025-08-25 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21ecfdfb-8633-38bf-ac99-e66c851f2a6f | -11.59792 | -46.36842 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 339c2aff-e7c2-39eb-8b62-82408f5c92c3 | -7.6546 | -63.52237 | 2025-08-25 04:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 447ad633-0115-30ec-bddd-a391ba76745c | -7.90918 | -63.07954 | 2025-08-25 04:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 715d6d2c-43ba-3b20-9e86-232fe447de2f | -7.90353 | -63.0717 | 2025-08-25 04:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 23.1 |
| cd8f1c0d-1c3c-331b-b1af-64ab6708cab3 | -13.61855 | -48.16054 | 2025-08-25 04:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85b33cf3-501d-3d41-a718-b79c569b9fd3 | -8.12598 | -62.87807 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2fca83e8-0687-3d9f-9bd6-97079c9820a7 | -10.71028 | -48.31417 | 2025-08-25 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08d59bc0-ea0f-3b9a-8686-77fdee79270a | -11.60898 | -46.23367 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e0b77b5-4b9f-3706-910d-51ba2f343c69 | -12.74118 | -48.13669 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d72bc336-1eb6-34b4-941f-17d6798746ac | -12.93656 | -46.30748 | 2025-08-25 04:42:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7dfbbb1e-baf2-3836-b111-99a28f123952 | -11.18216 | -55.02733 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84bb41c8-81d8-3f25-bd73-837b5eea6aef | -9.16156 | -59.49091 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 192bbb07-80cf-35b3-ba65-4f382ab47f88 | -11.17517 | -55.02094 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d58dbd7a-3e85-3807-8424-17325294e672 | -11.93365 | -46.737 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34fbca7a-0e00-3e64-9fb4-5acbcc33844d | -9.14452 | -60.73762 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee760b5b-535b-34e1-bfa9-37109d1a717d | -12.94307 | -46.31778 | 2025-08-25 04:42:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b307a475-ef9f-3803-b68f-1f0ac63ee384 | -8.88758 | -62.43618 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fb83ebb-152b-39ec-bd6e-5a6e7b4c4b8c | -8.62674 | -62.64312 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7340234a-6d5f-3df9-b6d9-2e6c20e1eda6 | -7.55153 | -63.86184 | 2025-08-25 04:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 557d3919-c2bc-3d64-9486-ee0ee7819e50 | -8.2114 | -61.38661 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a6afa9c7-698d-38ae-b5b2-8ddd2c4e06e4 | -7.79171 | -61.57079 | 2025-08-25 04:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da8a9f50-a674-39b5-bb90-865d253ec5bd | -8.86253 | -52.03882 | 2025-08-25 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1bfdb9ae-84c8-33c9-b373-d8094bb279dd | -9.26168 | -59.77178 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 30209b8f-4de1-30a2-b47a-40c355a0fd0c | -12.74998 | -48.1259 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0e9d13b0-1234-3f19-956c-e5e59dacb4b4 | -13.40253 | -47.52139 | 2025-08-25 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 43789126-c808-3762-abea-753559155919 | -13.45928 | -47.01502 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64aa9f83-4611-3343-a991-60f9c77a6ac4 | -8.90285 | -62.46277 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 29cb6ffd-6790-33b4-b81a-ca70bb71bf0d | -13.42954 | -46.89959 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2024005-cdce-37d0-8d17-2e831a78ffe0 | -9.18978 | -59.45969 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README50.md)
