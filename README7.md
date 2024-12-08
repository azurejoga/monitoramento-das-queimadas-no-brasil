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
| cfc93ace-dd78-3f54-a13c-15e5a21b2c65 | -17.82072 | -45.31673 | 2024-12-08 04:16:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 509c6c69-842c-3d1d-8dc4-c979d1774136 | -11.73427 | -54.31133 | 2024-12-08 04:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bc9c670-11fe-36d2-841f-450021bea3ab | -20.27315 | -41.33025 | 2024-12-08 04:16:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5a73cd24-151a-3345-9156-2698f314f681 | -12.78908 | -54.22075 | 2024-12-08 04:16:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6b1d2c1c-27c3-3be6-9f16-ae12b5a0e417 | -19.30356 | -45.54517 | 2024-12-08 04:16:00 | NPP-375D | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f589ac82-4c49-35c8-aab1-95289d90cf41 | -11.73498 | -54.30759 | 2024-12-08 04:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d029402f-b5d4-3608-9428-c89e6affea0d | -12.85464 | -51.94349 | 2024-12-08 04:16:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b070346-7203-3aab-8c1c-22ef8d4296e0 | -15.26214 | -53.57385 | 2024-12-08 04:16:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ebc0e6f8-bafc-3258-8238-dcc342f0c3b3 | -12.77751 | -54.22226 | 2024-12-08 04:16:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df16fd95-0578-3f49-b423-137d165d402b | -15.36628 | -53.1226 | 2024-12-08 04:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4145aec1-2aae-3ac7-99a7-8279d94304b0 | -17.1286 | -42.4156 | 2024-12-08 04:16:00 | NPP-375D | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d431d96-b350-310f-b280-29f5d4ebbac1 | -13.06839 | -52.04292 | 2024-12-08 04:16:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0996896b-639a-35b1-a2ae-14a104efe81e | -19.36164 | -41.51587 | 2024-12-08 04:16:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6d4764cd-8a8b-3e6f-8990-35ca3859d739 | -12.81141 | -48.57682 | 2024-12-08 04:16:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1790349d-227f-300b-9986-12b5478c542a | -19.26301 | -40.10936 | 2024-12-08 04:16:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 44990f1a-e1e1-3837-bf9c-87bbbebc93ed | -12.46935 | -46.949 | 2024-12-08 04:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa38dcdf-f77c-348a-973c-34a236adc511 | -12.53379 | -57.73655 | 2024-12-08 04:16:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 77500cc8-e2c2-3f45-af36-fd0abbc39115 | -12.53984 | -57.73547 | 2024-12-08 04:16:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d8c8926-0a04-3c72-89fe-289e80be6055 | -15.15882 | -56.47935 | 2024-12-08 04:16:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9aeb66d2-6631-373d-8997-37b22e128fcf | -20.75789 | -41.75244 | 2024-12-08 04:16:00 | NPP-375D | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 216e17f1-de36-3ecd-83dc-7c3643d2d623 | -12.86238 | -51.93618 | 2024-12-08 04:16:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbc40c3f-189f-32c1-bdb1-e9aaa54de7a9 | -12.53317 | -57.73375 | 2024-12-08 04:16:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ecb3992c-46c6-3a22-b40e-66a880a7d782 | -11.20968 | -53.82117 | 2024-12-08 04:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb971931-3342-38b6-ad57-53a01a8aea78 | -12.69259 | -46.7607 | 2024-12-08 04:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40f8c8cc-f37d-3396-83b4-0b7ee4c23f85 | -16.19863 | -41.05089 | 2024-12-08 04:16:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c2eb4cf7-a0ec-334f-a4c5-dfa23302c025 | -13.52197 | -43.51503 | 2024-12-08 04:16:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab88a2c4-ee12-3bcd-84e4-dc382d8a8ebc | -12.85772 | -51.93525 | 2024-12-08 04:16:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 213a1969-d4dd-3fc1-9034-d37168a22428 | -11.20942 | -53.82366 | 2024-12-08 04:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a7f63af-5af1-3ce9-b981-9ee24e16e8ee | -20.75397 | -41.75193 | 2024-12-08 04:16:00 | NPP-375D | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4842a680-c7c1-3cd8-849e-b755af89c824 | -17.16053 | -53.81026 | 2024-12-08 04:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f4735039-0afc-3abd-951c-8197c665b27a | -15.36522 | -53.12806 | 2024-12-08 04:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e9a2c27c-1c02-36bf-a566-fe1af1870dee | -15.25835 | -53.56689 | 2024-12-08 04:16:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9613124b-8097-324b-98d1-462ee29e7422 | -18.95412 | -53.69816 | 2024-12-08 04:16:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12458afe-b3bb-3ef6-829f-da0d4bdde068 | -17.72925 | -52.00633 | 2024-12-08 04:16:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4105600b-16b5-3663-b212-4593171ba3ca | -12.8504 | -58.22624 | 2024-12-08 04:16:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bef7715f-c6a6-3759-b8a5-b98fe25ac2bb | -11.20422 | -53.82019 | 2024-12-08 04:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96524088-2c17-368c-90e1-47cb020a6b2f | -20.20077 | -41.7891 | 2024-12-08 04:16:00 | NPP-375D | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e770f2e4-5b4f-3d53-b978-2ae3e4ac6296 | -12.54152 | -48.32743 | 2024-12-08 04:16:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcc06215-6a9f-3c81-aa57-752a9b116ee5 | -12.78225 | -54.22684 | 2024-12-08 04:16:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6fa15d31-3a5a-3c56-9461-8c12b8ab931d | -12.53856 | -48.32226 | 2024-12-08 04:16:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9b4eeb6-dc20-367f-ad30-44d0728fcba1 | -15.98182 | -57.17332 | 2024-12-08 04:16:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed1a08ec-5658-3877-9041-bf45924508eb | -12.41378 | -49.68869 | 2024-12-08 04:16:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ceef21b-de1f-3600-815f-9da069dc4119 | -17.12967 | -42.41383 | 2024-12-08 04:16:00 | NPP-375D | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ea62525-821c-3925-ac45-18582dfc2378 | -17.15892 | -53.80706 | 2024-12-08 04:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aeb3c916-2558-362d-be31-7e04c74a7ffd | -17.81289 | -42.94205 | 2024-12-08 04:16:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ef763e3-50a1-39ae-a292-95ed0c9c4f06 | -15.08854 | -59.63187 | 2024-12-08 04:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ebab3c1-b098-3831-b22c-36be7cf9488f | -20.26917 | -41.32957 | 2024-12-08 04:16:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 35aa4682-8563-3668-994d-84be33c2680d | -19.26426 | -40.11136 | 2024-12-08 04:16:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9fa93d1c-28a1-3c22-b50f-76b592a3c079 | -12.85178 | -51.93262 | 2024-12-08 04:16:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da582ce9-c0cf-3727-87c8-cb3a9fd1bd54 | -15.37111 | -53.12355 | 2024-12-08 04:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19851cfe-14ce-303c-bfa0-b416f0b1e23f | -12.85555 | -51.93848 | 2024-12-08 04:16:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ead75a3f-13c8-3dcd-96c8-0e37df73274c | -15.76737 | -45.08404 | 2024-12-08 04:16:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14321449-1282-3657-87a3-3a628380eec1 | -12.5929 | -54.38415 | 2024-12-08 04:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6489d49-f8fe-33c1-b33f-ebce9849cce3 | -15.08684 | -59.63937 | 2024-12-08 04:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 49a10c0c-ad08-3993-9b5a-c875b6b666e9 | -16.75534 | -41.05494 | 2024-12-08 04:16:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9607f5f7-b263-3395-bdb5-69f870bd8c2b | -15.26101 | -53.57955 | 2024-12-08 04:16:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b8eae550-edb1-3591-91c6-9fac3406df21 | -12.5423 | -48.32291 | 2024-12-08 04:16:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb75da78-a32b-3248-860d-f71159afba0e | -12.85212 | -51.9393 | 2024-12-08 04:16:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab20d4b7-f089-3ba0-9110-9d729fdb22d6 | -12.41037 | -49.68431 | 2024-12-08 04:16:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73a92332-c7b4-3b53-bf79-00bee0755b5c | -16.28924 | -48.02043 | 2024-12-08 04:16:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12690903-acc1-3db0-abd8-4f7502e49a22 | -13.08412 | -48.1129 | 2024-12-08 04:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45cf4bd9-1f9f-3fff-a032-c14ccaa88819 | -17.82016 | -45.32037 | 2024-12-08 04:16:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7dcc1402-1d4e-31cf-83d4-e5fcede6538f | -18.95875 | -53.6994 | 2024-12-08 04:16:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8229e749-b25f-3be6-b6b8-261ff20e846f | -15.2572 | -53.57265 | 2024-12-08 04:16:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 73ed4aaa-b0a5-373f-98f0-6d6c03a5b33d | -11.20396 | -53.82269 | 2024-12-08 04:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9402206-d850-32e7-bbbd-2bf529828f3d | -15.56872 | -47.85627 | 2024-12-08 04:16:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e112107-1494-3e37-a123-d0ceaf6d1a2d | -12.59677 | -54.38768 | 2024-12-08 04:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b00f74e8-498e-35a3-9713-8f2b331d437d | -12.86144 | -51.94113 | 2024-12-08 04:16:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7cc309ae-5f44-3b29-a197-8926bf19dbf4 | -15.76405 | -45.08348 | 2024-12-08 04:16:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa339d1b-5d3c-3fd7-842b-1fa583d5ee83 | -12.85088 | -51.93757 | 2024-12-08 04:16:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d971e8c-dfda-3c6c-af8d-d3b4b4da9b4b | -17.48067 | -51.83037 | 2024-12-08 04:16:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d78fcb6-47fb-3ab8-ba41-5fa9c6e09988 | -16.09151 | -45.19678 | 2024-12-08 04:16:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b39f3495-80ba-3e48-b09e-773bfa46f38c | -12.78294 | -54.22329 | 2024-12-08 04:16:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d4fba852-aa4d-37e2-a16c-24f1c54e0c52 | -17.8946 | -43.99734 | 2024-12-08 04:16:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1d8eed8d-fb6c-397f-a63b-601abba026e2 | -12.85306 | -51.93435 | 2024-12-08 04:16:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83d6599c-54a0-3302-89a5-03c5c49c3fa9 | -15.15974 | -56.47495 | 2024-12-08 04:16:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 098af1b6-ad47-3d57-9568-c6aa1fa3f96a | -12.68912 | -46.76011 | 2024-12-08 04:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43b3e054-c876-3207-bf6c-a42e25e1b03c | -19.53708 | -44.07929 | 2024-12-08 04:16:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa2f814b-4224-3a5e-acc4-beb7e236289a | -12.78768 | -54.22789 | 2024-12-08 04:16:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 028433af-5f92-3935-8056-4eaa6b6e866c | -12.40762 | -49.6763 | 2024-12-08 04:16:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9789e30-9ce8-3ed2-bb4e-13c69b17b2db | -19.07491 | -47.39145 | 2024-12-08 04:16:00 | NPP-375D | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7464124e-1b9f-3fc6-bd8a-d439f424ac37 | -15.0956 | -59.63388 | 2024-12-08 04:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ce0271d1-a005-31ac-b497-37f886f12aa9 | -12.123 | -54.28926 | 2024-12-08 04:16:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba9d7538-d44c-3139-9bfe-d68232f20aaf | -15.3503 | -39.87313 | 2024-12-08 04:16:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 97620995-89f1-33a6-9560-e1ae2f40bf46 | -15.25764 | -53.57167 | 2024-12-08 04:16:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c67f6614-af24-3579-be72-3e60f81eb5a1 | -16.6821 | -43.88526 | 2024-12-08 04:16:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53c0b53e-f026-345a-8499-68beb8bf3f57 | -12.53507 | -57.73064 | 2024-12-08 04:16:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18ca73fa-8ac6-365a-9a89-f940a0719b1e | -12.77682 | -54.22574 | 2024-12-08 04:16:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f674efee-713b-35a7-b72f-31a8668d70bf | -12.85645 | -51.93353 | 2024-12-08 04:16:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35a6b3b9-2fa0-3fdf-9b33-df7d32f473f1 | -11.21009 | -53.82017 | 2024-12-08 04:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57a307e3-4207-35d0-a5b1-ef8396b6abcf | -12.7782 | -54.21872 | 2024-12-08 04:16:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d00b3d84-4a71-3ccf-b7ae-deacf74e29f9 | -12.78838 | -54.22433 | 2024-12-08 04:16:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2e4c4c68-4d67-3e37-a67e-8b45b0c8f11c | -15.3508 | -39.8693 | 2024-12-08 04:16:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0d064e72-5048-3c63-b038-654ac2c48a69 | -12.5922 | -54.38781 | 2024-12-08 04:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f38ab60f-62a1-384c-929c-0b8e4da58742 | -17.67648 | -42.74414 | 2024-12-08 04:16:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 683087ce-4954-369b-a451-436b6d4d195d | -12.78434 | -54.21616 | 2024-12-08 04:16:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eb95faee-57ad-3599-967f-77f1691e574b | -12.8611 | -51.93447 | 2024-12-08 04:16:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09ba6bb6-5166-31e9-9793-869a86c69cea | -12.78364 | -54.21973 | 2024-12-08 04:16:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84dbe617-10b0-3a8f-adcf-fb2718f7ec51 | -20.2233 | -46.40236 | 2024-12-08 04:16:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a132298e-825c-3bda-99e0-81e9984ce5c4 | -12.85678 | -51.94021 | 2024-12-08 04:16:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README8.md)
