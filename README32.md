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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ace4decf-0170-37ed-8231-7e7fa37e7f57 | -18.40569 | -42.86076 | 2025-09-22 04:40:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c943e061-60df-34a3-80e6-f12a19add96f | -12.72451 | -46.83574 | 2025-09-22 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a416fcb-3abf-398f-b517-555eb290241d | -11.46262 | -46.94083 | 2025-09-22 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af82863e-0925-30db-8ab0-8d424783830b | -20.25776 | -55.50233 | 2025-09-22 04:42:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 06029fac-37b9-355b-8e46-f08d9eb1a1c6 | -19.24894 | -46.54945 | 2025-09-22 04:42:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c352b263-e8c5-3830-92a9-106509e061ab | -19.86161 | -46.10273 | 2025-09-22 04:42:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c73982f-d6e5-33cf-8534-38c2025fbad5 | -20.26481 | -55.50375 | 2025-09-22 04:42:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 62c47495-8064-3312-b396-23d16a5143b5 | -20.43566 | -43.67654 | 2025-09-22 04:42:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ff796eae-b2ba-3b14-8601-fa084ebba9b8 | -19.64642 | -57.73979 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 7b572415-14fb-3092-8c37-35e61912fc74 | -19.85999 | -57.30256 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 3d664367-b1f2-3ea1-8c33-c23192df8630 | -20.6691 | -54.57335 | 2025-09-22 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16c27455-7db0-3818-a880-239c6ffcfa1f | -19.65041 | -57.74063 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3ca5fd3b-9450-3f78-a7e0-7e60f90413d8 | -19.85128 | -57.30611 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 65486572-1c1f-3837-8114-0b181df22914 | -20.12458 | -42.47941 | 2025-09-22 04:42:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c3851376-6e79-33dd-90f0-b5fb77073bf2 | -20.4013 | -54.86485 | 2025-09-22 04:42:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 249d0c99-76a7-3e89-88b0-87d02ef0e1c8 | -20.47573 | -54.53263 | 2025-09-22 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e055356a-8aa5-3be9-9ee9-b2fe83c827cf | -20.26906 | -55.50024 | 2025-09-22 04:42:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 24a9ca1f-44fb-35ea-8dd4-ec37c0c8aeed | -20.25703 | -55.50655 | 2025-09-22 04:42:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d49ae5f0-61ab-3e97-9f47-8eb84e59c708 | -20.25847 | -44.42195 | 2025-09-22 04:42:00 | NOAA-20 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 5fdf8f21-57f1-37c1-963b-c46b26e96662 | -20.54963 | -56.15458 | 2025-09-22 04:42:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b672fca9-6f08-31a6-90ef-f52d10fe3f20 | -18.98511 | -44.22787 | 2025-09-22 04:42:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24be5f5d-2284-378c-bfb1-dbbf39fa4bef | -22.4175 | -46.79245 | 2025-09-22 04:42:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e1fb661-ff1b-3e51-a650-093241062dc5 | -22.73618 | -51.41566 | 2025-09-22 04:42:00 | NOAA-20 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| af0753e3-7d12-37d1-9b8d-f6ec6f9aa467 | -20.26129 | -55.50304 | 2025-09-22 04:42:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| affb8a6c-2a66-3862-ab9e-316f5c0cc964 | -21.83342 | -53.94364 | 2025-09-22 04:42:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5017171e-ad3f-3183-8c8b-128e0c0b576a | -19.84627 | -42.20882 | 2025-09-22 04:42:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9106f62e-8548-37f5-a976-4513aa7f0c22 | -21.13091 | -54.481 | 2025-09-22 04:42:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef56e2a3-c0d9-317b-8cae-0f250329f003 | -19.85317 | -57.29575 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5d67a7cd-7d40-3488-8106-88d226160ff9 | -21.84097 | -53.96058 | 2025-09-22 04:42:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| fd343432-614d-37c3-a86e-f7928d6a94a2 | -20.3989 | -54.86549 | 2025-09-22 04:42:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2227a1bb-b5e4-33ed-a189-70d2d25b8c25 | -19.57398 | -41.65699 | 2025-09-22 04:42:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1fd4ebf8-451e-3838-bb7a-53ec1d8c8065 | -21.37043 | -46.17491 | 2025-09-22 04:42:00 | NOAA-20 | AREADO | MINAS GERAIS | Brasil | 3104304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a61c8b58-5d0a-3f18-8119-1c7e4db56b9b | -19.84515 | -42.20235 | 2025-09-22 04:42:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| bbe6ace1-b9ac-3d6b-9400-c1a0e1a0132f | -19.43063 | -44.81976 | 2025-09-22 04:42:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d27e5ebe-ed0b-3b79-95ca-db795a00dd2c | -21.83219 | -53.95117 | 2025-09-22 04:42:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d65802c9-385c-385e-9042-f1c5d2d0db7c | -21.58101 | -46.93129 | 2025-09-22 04:42:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bfd7a49-2247-3df7-94de-5fe94c1396ed | -21.9199 | -47.31719 | 2025-09-22 04:42:00 | NOAA-20 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a2475fda-6d55-32d3-b89a-ae26d6e61160 | -20.6651 | -54.49221 | 2025-09-22 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f6ff16db-6918-3fe2-afa1-46df76bdcb57 | -19.81356 | -46.39503 | 2025-09-22 04:42:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d1f4f1b-5661-35e7-8f85-21ca98034b73 | -19.80879 | -46.39865 | 2025-09-22 04:42:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04ebec9f-fbb9-3747-8a12-a65cf0b40cca | -19.59312 | -57.73617 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9418fffe-855c-3e40-8c88-7e0086b07a0b | -19.85525 | -57.30836 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 496be258-95d9-3cc3-bd59-a1d71b22d36c | -20.55041 | -56.15015 | 2025-09-22 04:42:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e38a37cd-5453-3a7b-8af7-949be0be547b | -19.85905 | -57.30774 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e1d76ed4-300c-3490-84b7-0fed560a399c | -21.13727 | -46.33711 | 2025-09-22 04:42:00 | NOAA-20 | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ed044448-3fad-3fd4-b76d-92b46884a676 | -19.43914 | -45.17761 | 2025-09-22 04:42:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18f99979-c7db-37f3-8a05-2bf898822e7d | -20.66848 | -42.2865 | 2025-09-22 04:42:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 306f90ad-4dc9-34aa-aeb0-7b39765129d2 | -20.43601 | -43.67304 | 2025-09-22 04:42:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 964ed8a8-03bc-3043-8ca8-2100a9e31e79 | -21.6458 | -54.40171 | 2025-09-22 04:42:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 05ed89f0-3657-3586-a67e-a20e8c482fd2 | -20.25351 | -55.50583 | 2025-09-22 04:42:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 79a9ae4e-db9b-3b1b-8998-a3e0a2f3fed7 | -20.37501 | -58.06055 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d3416f1e-09f3-3ab0-a604-fca1df6230e6 | -19.86711 | -46.09361 | 2025-09-22 04:42:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8805ccbc-a2c9-3e4c-bb76-7fed02e9f7c9 | -19.84635 | -57.28895 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 81ca73c8-5d32-3307-9ff2-2faaa585069d | -22.9484 | -46.08104 | 2025-09-22 04:42:00 | NOAA-20 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 72ae4788-7009-3f38-b9e9-62018dc1aab5 | -20.67267 | -54.5731 | 2025-09-22 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e0d1c95-7a07-3bcf-8c2e-00c244b89ee3 | -19.84476 | -42.20636 | 2025-09-22 04:42:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9b8d6d05-e6ae-3f71-9188-43d20be920b9 | -20.18648 | -44.62238 | 2025-09-22 04:42:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89db1dc0-4740-320b-b748-d12958b10389 | -19.85136 | -57.30756 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b4f6aa23-f203-37c9-8036-2104451c08a3 | -19.64973 | -57.74431 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 88f121bf-f084-343d-9ef9-813cece12dd8 | -19.86596 | -46.10329 | 2025-09-22 04:42:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 888c4d09-85bb-3a97-b7f6-85fb4a8e7330 | -20.54601 | -56.15386 | 2025-09-22 04:42:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df53656a-d363-3474-93da-386f9bc12502 | -19.63376 | -57.74094 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 5742e821-e56c-3e34-bc8a-d2f54f7f3657 | -19.85622 | -57.3032 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fba69153-67f7-3203-a5bd-c7649181f29e | -19.84668 | -42.20482 | 2025-09-22 04:42:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 0ec873b8-6ae7-3a7a-8be4-561ef20f0dcb | -19.85023 | -57.28977 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 13b171ec-e0aa-3992-ad03-6e6ffeb5c2e3 | -20.67191 | -42.2862 | 2025-09-22 04:42:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c020e427-0d89-3c09-a4e4-df54f4a80bab | -19.84024 | -42.21227 | 2025-09-22 04:42:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e63728b6-de0f-3979-8f87-b6ea69558b4c | -20.12923 | -42.48928 | 2025-09-22 04:42:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 40fffa92-d32e-3bc3-968f-5a3e4fdc97e2 | -19.89755 | -44.60009 | 2025-09-22 04:42:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3b547255-0735-317d-8f7f-70b81f32461b | -22.3076 | -46.70409 | 2025-09-22 04:42:00 | NOAA-20 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6afc8d1d-6748-3149-b45a-c61988df962f | -20.25424 | -55.50164 | 2025-09-22 04:42:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 538cac53-d829-3a52-a8f5-58b5ffc6c2b0 | -19.27925 | -43.74392 | 2025-09-22 04:42:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc142205-7150-30c0-9741-733595eda235 | -20.12497 | -42.47532 | 2025-09-22 04:42:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7d9b1b67-2d86-351e-ba68-42b06be815bd | -20.40234 | -54.86612 | 2025-09-22 04:42:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67e9e31e-9f05-34c6-8440-e9cb287e9111 | -20.18593 | -44.62726 | 2025-09-22 04:42:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 453e9167-263a-33e5-9178-6914832b6a71 | -21.58152 | -46.92703 | 2025-09-22 04:42:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2220cb00-7e31-3258-ba9b-332b4fe15113 | -19.31351 | -43.7577 | 2025-09-22 04:42:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6c2fe146-1d12-383b-b25b-21cdc2d535b7 | -20.67155 | -42.29011 | 2025-09-22 04:42:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9b3c1c0c-4d7b-3503-bddc-6651a6bddaf4 | -18.4053 | -46.86211 | 2025-09-22 04:42:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b1489eec-6c3a-3876-b311-9abbf192be16 | -20.43872 | -43.67675 | 2025-09-22 04:42:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9271b472-a239-30d7-9cf5-dd40c1cd7069 | -20.54679 | -56.14944 | 2025-09-22 04:42:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b5b7b6a-9784-3840-b460-c4701d464217 | -20.4748 | -56.65664 | 2025-09-22 04:42:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 47a1fc53-a034-3ac1-8778-59766a3e1e44 | -21.16503 | -54.63153 | 2025-09-22 04:42:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9470114d-2b16-36f5-809f-16c6e30fc6f0 | -20.99224 | -54.76085 | 2025-09-22 04:42:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7c707f4-6328-3edf-a27a-bef69dd38aad | -20.26626 | -55.49535 | 2025-09-22 04:42:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 99b6284e-b865-3c54-87b4-8088195e2523 | -22.30377 | -46.69934 | 2025-09-22 04:42:00 | NOAA-20 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ade6022e-8cd5-38bb-a7c2-a697c1e069b8 | -19.62645 | -57.73557 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ccfba0b2-db2e-341a-9d02-990d9138b57d | -19.85234 | -57.30238 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f35163b4-5e9b-39e2-922f-1780a8b677b1 | -21.83763 | -53.95996 | 2025-09-22 04:42:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 599f6a30-aed9-3498-83e8-da08cc57f871 | -20.39957 | -54.86152 | 2025-09-22 04:42:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d63ca6b-0a5f-3914-8a50-640d70a33f9f | -20.85621 | -55.1688 | 2025-09-22 04:42:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85650452-ed5c-3af7-bfa1-81f81a3d7893 | -22.30428 | -46.69501 | 2025-09-22 04:42:00 | NOAA-20 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1319b1e9-e752-3749-a7cb-87887606403e | -20.66994 | -54.56854 | 2025-09-22 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53620dfa-1c26-3fdb-97a1-e6daf6cd14b3 | -21.83552 | -53.9518 | 2025-09-22 04:42:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a164b132-cea3-305b-b4ff-242f65bd24ee | -22.41698 | -46.79675 | 2025-09-22 04:42:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78c3b403-6bbf-3a5a-a188-cc69db9cfd7a | -20.99498 | -54.76542 | 2025-09-22 04:42:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee60ad99-6802-309a-9a3c-d7fa5778da65 | -21.64587 | -47.49149 | 2025-09-22 04:42:00 | NOAA-20 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18df75c8-3c88-325f-8cc2-dd576a860558 | -20.66927 | -54.57244 | 2025-09-22 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96a1dd26-db52-36a5-8e1d-4c79f72ffd01 | -20.25849 | -55.49815 | 2025-09-22 04:42:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e505ba3a-16af-325f-967e-362b253e6865 | -20.46403 | -45.00024 | 2025-09-22 04:42:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README33.md)
