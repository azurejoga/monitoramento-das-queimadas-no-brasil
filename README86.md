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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b80d4ff8-c0e0-313f-8527-0e0961d2c8cc | -3.65521 | -58.87068 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af934ab7-183d-32ec-b854-9f26a6fc01ac | -2.94791 | -51.03824 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 397f0156-276c-3edb-9c5e-2a5548aec55e | -3.23578 | -60.80475 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 176e0779-504a-3db8-83a7-990deaecdf53 | -3.29555 | -57.86349 | 2026-09-21 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7561bdd2-ee0f-3ec7-88ad-a29c18131c2d | -3.65105 | -58.8741 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1966f60a-b0f1-37c8-86e1-0a2e2f955bcf | -4.35433 | -55.66018 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e43d3329-8087-383d-92ee-27f6be022ea1 | -4.26091 | -55.77122 | 2026-09-21 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f18f0ab-9102-3c96-8f52-91425ad779cd | -2.45922 | -49.22171 | 2026-09-21 05:40:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f7c5e7c7-34f8-3781-ba5b-8699af792b31 | -3.45934 | -60.52053 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1de6b7d6-af58-3345-8e45-43a0ed9d80d7 | -3.75954 | -59.42615 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dad0e5d4-ee85-31a1-9d00-370e19bfae1f | -3.37813 | -50.44066 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8435f996-ac83-30e5-b217-3c1c915d6d4f | -3.07672 | -61.16706 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c6e44c5-9368-3e17-b6e0-929eed774773 | -3.34767 | -59.85274 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c32df67-d60a-3c19-8622-cf2aaa0d78ed | -3.5484 | -56.88869 | 2026-09-21 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ec8d02d-1402-3a1d-b6f1-21a212942e87 | -3.1721 | -51.35913 | 2026-09-21 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c056fee5-ee52-3212-a56d-50cab99105da | -3.65813 | -58.87519 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04e44d4c-a1ca-3ee6-9144-faf5cca246e0 | -3.49312 | -59.61193 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dfedd599-1d7d-3648-aac3-c96c580cf54a | -3.06795 | -59.16902 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a78ed2ce-805b-38aa-a00f-bb621d04c3ec | -2.91778 | -57.79283 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e9a2ae9c-bc8f-3f03-8843-feda132e1493 | -4.07227 | -52.12873 | 2026-09-21 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6116f61d-edfb-3997-84c7-6a520402811b | -4.30272 | -56.26317 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3b7e7b5-451c-3250-9e89-8f52a6ceeb64 | -2.616 | -51.73135 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96f83fcd-9e81-3dcf-a1c3-5a10cb3db103 | -3.47801 | -57.98096 | 2026-09-21 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6dfa437-9e8f-3183-bca8-a4b20c59a00c | -3.13839 | -61.22618 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9cf9b17-9f00-36d4-ac9d-525b45fdcfe7 | -4.87995 | -55.88715 | 2026-09-21 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32eaa18a-e45c-38b0-8e86-602c66863c44 | -2.88072 | -57.78711 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e804ba12-6ada-30c4-9fe6-b890b8bf00ad | -3.27297 | -60.88525 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 39976e3d-145a-3ce4-a048-917abdfa38b2 | -3.82357 | -59.33521 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 113de8cf-79e1-33fd-86e4-6fd9532fbccf | 0.79145 | -59.20196 | 2026-09-21 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddc5d92b-fffb-382a-a583-543c4e724705 | -3.22966 | -60.80023 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58afebbd-2945-3be4-87bc-9e18dca5fc0f | -3.33406 | -59.80585 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22782b3a-9233-30d5-989a-7d10e9a64102 | -4.15938 | -59.9274 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21ae69b6-a61f-31ac-b1b3-ec53443188d0 | 1.53855 | -55.80631 | 2026-09-21 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 679e58f1-89ee-3c99-a075-7f68ca1a0096 | -4.2336 | -56.20228 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 204ad2c7-a345-3ff2-a4c4-f7a114208efb | -2.94714 | -51.04391 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01af2014-a369-334a-808f-0caadffff5be | -3.49084 | -59.60399 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab094b7c-806f-3438-ad1f-3b8aae730464 | -3.04422 | -61.26463 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93cfee98-c5a0-315d-8f46-5b3eb9f356b5 | -3.43742 | -58.02335 | 2026-09-21 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a23e9d4-a4a7-341f-90d7-6c259676e593 | -3.75608 | -59.42561 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e0d8aeda-ac3a-3c1a-98a8-10216d513a86 | -3.30488 | -59.45462 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a978c4e-0b98-301a-9a54-3c9b3ca68a32 | -5.01622 | -56.09149 | 2026-09-21 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 057bccd6-9437-3cb9-81e3-5ab3e3c6f0f0 | -3.66415 | -58.85991 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a22f2d1-f237-36f0-a259-991dd4f9ead9 | -2.91104 | -57.78732 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cc2b0bd0-b56f-3d35-85f8-35d6b44bb829 | -3.07526 | -61.28365 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3c4b7ba-63b4-36e6-832d-e18f3a38aa82 | -3.14867 | -61.39766 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2d6f2f7-960c-3b76-bf1a-69b07b08106e | 1.54864 | -55.81928 | 2026-09-21 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6102c9a8-b7b8-3ae1-881b-d0485ecc47fc | -3.38789 | -61.29712 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 137f3b95-9ee7-3752-9c54-d5081f71b09d | -3.08614 | -61.17208 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2df3e03a-9eae-3445-8a99-c1dc494f934a | -4.34939 | -55.66361 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 287af8f2-9de9-3011-ac92-22006233fe0e | -3.1116 | -61.41662 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68d16ef4-3714-3ea6-87da-b7617350a6df | -3.54263 | -58.94706 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acc9347b-ba3b-337d-926c-23a77389e84d | 2.00953 | -55.85051 | 2026-09-21 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9cc11221-9ead-3c87-8c1f-c9b767161651 | -2.88997 | -57.64677 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08509767-81fd-348d-8eea-bd926c67c374 | -5.01565 | -56.09534 | 2026-09-21 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c565fce9-2fce-3aa3-853a-5a332475764d | -4.09573 | -52.12423 | 2026-09-21 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e3e73649-3fa3-3f67-828f-a706d68f94fd | -3.82539 | -58.88656 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b79263c-9769-36f8-9b6b-915112b22a59 | 1.39019 | -50.92229 | 2026-09-21 05:40:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2975db6c-78b3-3bf5-a158-fe742ab69878 | -2.74274 | -54.58475 | 2026-09-21 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 747a3d21-75c7-36e3-a7ce-221eed9e0f43 | -3.68636 | -60.62821 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5c0a3340-6116-3cea-937c-2257836e6c44 | -3.42975 | -59.25724 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c568aefb-a8f8-32de-9a70-51839aaadbed | 0.78864 | -59.20605 | 2026-09-21 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa9aa62e-ac27-33cf-8dba-318d76e8802d | -2.50628 | -56.60244 | 2026-09-21 05:40:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 118f08d1-143f-361e-b1ad-65fafd1c6a4a | -3.48916 | -59.56957 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb099550-d05f-338c-9c08-186acc83967e | -3.14922 | -61.39421 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ba08a01c-c0a1-32d6-8bf0-17ce8f208a3b | -3.44831 | -59.25235 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91f61a30-0d49-3875-a913-e28639cca193 | -2.45842 | -49.22693 | 2026-09-21 05:40:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c60dced9-49c0-3333-a024-ba954878de4a | -4.23417 | -56.19852 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a37504e-196b-3f6b-899a-9993230e5447 | -3.07358 | -61.27277 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2482040c-6baa-34a2-83ae-2dec62eeb70b | -3.00903 | -54.167 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4862156-3f9f-3951-ab2a-2fb513cb7ac1 | -2.8748 | -57.81509 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c579cd10-d9c6-3385-9316-3656ff4e3420 | -3.01293 | -54.17278 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53948c05-f5b1-324a-99f9-ee42c8041029 | -3.34597 | -59.86364 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af99b88d-d260-35d3-bc1a-d871d33c6dd8 | -4.07322 | -52.12455 | 2026-09-21 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca97062c-0388-3da8-9963-cf4a892cecd0 | -2.99888 | -54.17044 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ce65d43-f768-367e-b1ad-fc429dbc10ae | -3.68855 | -60.59256 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0662335-dff0-3e56-b335-5076bc6612f4 | -3.15117 | -58.63963 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 630ad48f-bfbf-3f35-88bd-49fae471d99f | -3.16546 | -48.61296 | 2026-09-21 05:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85e3f820-e59f-3e49-bdc3-331e9693d2ed | -3.29184 | -57.86293 | 2026-09-21 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3124a25-3bab-3156-b41b-2be212a9e2a4 | -3.69299 | -60.56441 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c540c02b-598f-3f3b-b713-cb4fc366a83b | -3.38179 | -61.29262 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02966419-d79c-34e4-a5d1-3739c3b1e81a | -3.48629 | -59.56533 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60c9671c-e42a-33f3-9ca2-6f5c1895e7ce | -3.45581 | -58.21793 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff97d8bf-7871-35f1-a443-556cdef071d5 | -4.26152 | -55.76725 | 2026-09-21 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6abeaec-7dc1-30b6-a79b-3a024beba55c | -3.66161 | -54.27443 | 2026-09-21 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cb250648-9f6d-3083-8c8d-2f07280d3210 | 1.74244 | -60.57456 | 2026-09-21 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b70fd2ff-c3ac-37f8-81b5-391823f13f6b | -3.34427 | -59.85221 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16e5fecf-cb09-38b5-93f9-7dbac5ad376e | -3.69953 | -58.93306 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6474db57-be69-3a72-ac39-935406fa80b8 | -3.44692 | -58.39485 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0e6cc87c-b53d-31a1-9d17-882251d17ddd | -3.65353 | -58.85827 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d68760a9-5a52-3318-8c53-9ffd066009b1 | -3.26909 | -60.88821 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07e42535-98c4-37a5-b426-5ec4eee0cee7 | -3.05919 | -61.27759 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 112e50a0-a87c-33d4-8508-d753e3cd8aa6 | 0.69005 | -59.55129 | 2026-09-21 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d66323b-456a-3a7e-a667-6fb5b5f0729e | -2.90331 | -54.18436 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab22b355-c6bf-3457-aeb7-14234c3138cf | -3.65291 | -58.86222 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27f0f858-8c93-3125-aa85-0a7e67eea770 | -2.21502 | -60.17606 | 2026-09-21 05:40:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 052b5b0b-c22c-37fd-a79f-29c320c65e62 | -2.65995 | -59.76269 | 2026-09-21 05:40:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eadeeb53-536e-320c-b476-3138e768553e | 1.55033 | -55.8046 | 2026-09-21 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57a34f2f-5f7f-3037-a0c2-67ca19eb13fa | -3.47883 | -59.59074 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6099f7d-11c8-3e49-95e6-265b4ec7cc5b | -3.05696 | -61.27016 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e83c744-18cc-32c1-a632-3c9a17af4b76 | -2.99967 | -54.16531 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README87.md)
