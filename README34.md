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
| 3cb9a5c4-3c12-3d9d-bc76-afb173e49ba5 | -14.70978 | -48.1957 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e31fead-9771-3df5-a097-35b856200dcc | -13.30036 | -47.59515 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e6675a7-fc32-31cd-8e67-543cd63b729a | -17.08507 | -46.24429 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 66b5f196-2b26-318c-8e36-230f92677d58 | -16.14587 | -47.99241 | 2025-10-04 03:53:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3ded53a-18f9-35b0-9fcf-56718d923c80 | -13.51945 | -47.27424 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b61c58bb-57b0-39b3-9ab6-b1dc9e042185 | -14.67687 | -48.27639 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f00af47a-eb6d-39af-b8c4-ad057a9fddfc | -11.10211 | -49.84918 | 2025-10-04 03:53:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e259f15e-4065-3066-8697-cceb6440a8ff | -14.23109 | -46.08689 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8bedf3d-4bc7-3d46-9c88-05e0d9efbb3c | -13.99247 | -48.20314 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7af78c8-cf76-3060-98a0-29885cf9b016 | -14.64804 | -48.30827 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 20a14232-ce3b-3c2b-945e-aa1eafb0deb6 | -13.09933 | -47.89119 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b945f5ae-eceb-3fec-a777-53bea64d6713 | -14.89358 | -48.3562 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f391c239-7d3d-3a26-96c5-1fa233dd3d94 | -13.75052 | -48.051 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d4d29022-a7b1-30f1-a413-828b64c70136 | -16.02236 | -50.94684 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3dc5767a-b167-3e0a-86da-040e34263f03 | -12.10759 | -43.44235 | 2025-10-04 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb3baec4-73c1-377d-9cda-6002fc85774b | -14.42803 | -46.08834 | 2025-10-04 03:53:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8bdadc3-ce40-32f3-9294-5a02461e94d8 | -12.02212 | -45.19981 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f49e6ff7-fd30-3c57-a104-c9ddfbd668d6 | -11.92198 | -46.39756 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 92202b79-f281-3ccb-b8ae-e009de480f55 | -12.64583 | -46.9935 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d75d977b-2de2-3e7d-9eb1-8bc526715146 | -14.22163 | -46.08542 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ca09374-ad73-3fcc-9844-f57213b963e5 | -15.31624 | -46.37797 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01ad2cec-d3bc-3854-aa52-4439a1b90212 | -12.65459 | -46.97569 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93a4bc3a-b165-3fb8-adca-7fd9538aade2 | -14.66249 | -48.2922 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 31.4 |
| ee841d8c-653f-373d-8581-5fe6435a0a71 | -12.09304 | -45.17153 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbd620be-cdea-3b31-a417-ee76d948e3d5 | -11.68978 | -47.50071 | 2025-10-04 03:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fdc8f90-0654-3d33-b8c1-c95ef0776788 | -13.59382 | -48.18077 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b745e57e-ee10-3d4a-93e9-fac432680d70 | -15.65475 | -46.25681 | 2025-10-04 03:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32c4df26-dc86-3c45-95fb-20d6cf5f73a1 | -15.58922 | -52.46602 | 2025-10-04 03:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e1dadf07-89fe-3f3d-9bd8-817aaa585b8e | -13.40511 | -43.69172 | 2025-10-04 03:53:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fc7fa9a-06e2-3b7f-b296-950947e3efac | -12.11176 | -43.44269 | 2025-10-04 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1335dd97-e7cf-3515-9fd9-9767c5810421 | -13.33053 | -47.19521 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6297f0d-9ecb-31a4-a55e-f59f579205f7 | -17.5505 | -44.42336 | 2025-10-04 03:53:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efa02b52-957f-31d8-aa7a-c47913bce11e | -12.81558 | -46.86367 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85eb4c9c-919a-3c0e-b51c-b3c2c4290d62 | -13.32206 | -48.1199 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a493371-efe6-34db-afe3-6108ea1736e7 | -13.81579 | -47.58417 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 916f621f-d1f3-36b8-bf2b-dc18b2346bc7 | -11.27946 | -47.80033 | 2025-10-04 03:53:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e6fb77f-6ab8-377f-a5f6-d88773804e36 | -11.79302 | -46.82578 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 37e12be1-4708-3f6c-b811-394d452a2e58 | -11.91265 | -46.25628 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b79824c5-7757-3fa4-badd-69de823b020a | -17.08059 | -46.24331 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ae5b70a0-46be-3b64-a998-c93ab5d91f5d | -15.60277 | -52.46896 | 2025-10-04 03:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 35e28be1-cace-3ad6-9f42-2d81b737cb86 | -14.23693 | -46.08178 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cbf3861a-4c08-3627-8e69-64adce4d435a | -14.23789 | -46.07674 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 168d99f3-bd20-30fb-a0b4-d5fe4f81ffb0 | -13.73575 | -47.95732 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20c69b71-82ac-31f4-94b0-958fb66d1e94 | -11.9092 | -46.38304 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5451a53d-3ec5-3f35-8d8a-f30b64985b95 | -13.33278 | -47.62556 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 993e9bb3-4401-31ee-bbcf-3644c3243faa | -14.88821 | -48.29964 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| adfd26a2-8d1e-38c2-ab47-70f73eb7b16a | -17.45043 | -47.48007 | 2025-10-04 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e50327e-b387-3094-b530-2b2af6821a4f | -11.25959 | -47.79348 | 2025-10-04 03:53:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a1b7250-1181-3f48-b77f-0dc41591bec5 | -13.31041 | -47.5718 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49919e61-1b2e-311f-b912-fb0199eac5b4 | -13.21139 | -47.81178 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7b5989f-1b44-36d5-b811-98b2869e7115 | -17.98908 | -45.00874 | 2025-10-04 03:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0465665-942e-3a14-9c38-507ad57ac44d | -17.15722 | -47.0457 | 2025-10-04 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b50d76d8-79e4-3ef1-8928-8df432598d5c | -14.29173 | -47.41961 | 2025-10-04 03:53:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4f2e0946-a7bb-3782-bf90-61c3063449d8 | -16.04523 | -50.93085 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 54122f4f-4141-3418-81c0-f9695ab2cc57 | -13.3284 | -47.61987 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ee26dd0-1a2c-38c4-87bc-a699d2b185ff | -11.91603 | -46.73766 | 2025-10-04 03:53:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0220383-711c-3264-ab48-5262c0adfcbd | -13.5259 | -47.24066 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| efb250b8-ef1b-3c48-bc8b-e38c11fefc41 | -14.43171 | -46.09444 | 2025-10-04 03:53:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20a624aa-dfb5-3ff3-acd4-2a2aa6065a72 | -17.08451 | -46.24176 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 088b8a60-287e-3937-b097-f5eecbd4bb9e | -11.80396 | -45.03083 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ac72358-2ce1-36b4-89e9-f58f7b6a9908 | -15.52702 | -46.82042 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fafd1c07-2b75-3125-95a9-5f513ee21863 | -15.5823 | -46.91091 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac70ab10-041a-340f-abd1-5974fd8b3e78 | -13.74149 | -48.09642 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0c1035e-02e0-319f-88a4-3acf4c139d19 | -14.19417 | -46.07136 | 2025-10-04 03:53:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8af5bec6-bc0d-359d-8d7c-74c5a948a5e6 | -14.4452 | -46.3834 | 2025-10-04 03:53:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6be775f2-ac38-38ea-8e55-15e83f24437d | -16.35573 | -51.4721 | 2025-10-04 03:53:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fc3cd305-7121-3aba-a446-40949348eba7 | -15.69284 | -46.27122 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e43539c-9b66-3f2e-bb94-633f6cc37608 | -12.84905 | -46.85331 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16e0d6dd-625b-35c8-b815-8392678b22c8 | -14.19322 | -46.67873 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d796087-8c24-3a8a-a829-7bbf2cc004c3 | -13.74172 | -47.9553 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fb8abe3a-5760-3fca-8534-000f35e13df2 | -15.61271 | -46.93526 | 2025-10-04 03:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 022247f1-f638-3935-9c57-d9db62d61fae | -13.93159 | -48.16971 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 70c6073d-f40b-3abd-941b-33542363b783 | -11.87924 | -44.98032 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f413f1b7-5816-3009-b695-2d32f4136abd | -13.20872 | -47.80685 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6334785-ac99-325e-b734-5df80c700ba4 | -13.10976 | -47.84697 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2c0b31eb-0b14-341a-88dc-abcf5c9ddae7 | -13.31943 | -47.24755 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0a1252c-c80d-30ab-bb40-eca0e30e7231 | -11.82669 | -44.90865 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e057b008-2a83-370e-9bc9-24427095b853 | -17.07823 | -46.25023 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1eae0e3-fff7-3ca3-b905-6f07d584b733 | -16.00874 | -50.93082 | 2025-10-04 03:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 46c3c05f-e5ce-309d-a8f6-a1225d5fa610 | -13.20678 | -47.80687 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90acedd0-809f-3adb-8bb1-ab027070e86c | -11.66338 | -46.9924 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 020c4b55-9048-3e10-93b0-633f3b88c6ee | -17.99239 | -45.01372 | 2025-10-04 03:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0841db4b-8345-3f75-a343-3b2eee338a18 | -15.95468 | -43.32806 | 2025-10-04 03:53:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b9e9b7f-42f1-3071-9210-5ab2a1b85851 | -13.51929 | -47.24733 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1615a9a8-932d-3068-be6c-2f5099b18d4f | -16.36035 | -47.06664 | 2025-10-04 03:53:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e11dd3ba-c40b-32cf-81d2-e9fd60f6b375 | -14.65433 | -48.30487 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a133461-8139-3784-8fe7-92839359f79a | -14.67394 | -48.26321 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 079a9bfb-dc8e-3767-b751-0070855708ee | -15.66516 | -48.14825 | 2025-10-04 03:53:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 522a595c-58e4-3d4c-856f-afa948f156f7 | -17.55951 | -46.75767 | 2025-10-04 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b586315-9994-3b24-9711-b2dc1c5750e3 | -16.39324 | -52.16286 | 2025-10-04 03:53:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d2deb505-c4e7-396f-8925-5e3392338b17 | -13.3263 | -48.09842 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f6ba0e1c-2333-329f-a250-1c81b9a0576d | -13.33103 | -47.19267 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65604fbb-aa9d-37e5-9c4f-ae9c1e775c20 | -13.11018 | -47.92935 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7deb228-504d-3923-8cd4-ace47fe56396 | -15.65391 | -46.26122 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35ad6653-cce9-3ff6-9b54-fb1c163faa9d | -14.19511 | -46.06634 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 74ba9ef7-7b44-3892-894c-a4350434201b | -17.08151 | -46.23863 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f765617e-67da-35f8-a5cd-4cf1b36e1031 | -15.35107 | -46.29625 | 2025-10-04 03:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0295598a-182e-3305-bc6e-2e7906ab3bbb | -15.52625 | -46.79864 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f780a2f-0317-39a4-9505-a591e639bf7c | -14.88735 | -48.27633 | 2025-10-04 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 19b96a2e-4810-362d-b420-fc521835f230 | -13.26966 | -46.47557 | 2025-10-04 03:53:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README35.md)
