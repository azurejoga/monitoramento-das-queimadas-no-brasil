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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 701c611f-fc97-36f7-8002-67b337b6dd43 | -18.591801 | -47.289902 | 2024-10-07 01:19:50 | METOP-C | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9bdc6687-bc5f-3abb-b03e-054b9d8ed66e | -18.5956 | -47.304001 | 2024-10-07 01:19:50 | METOP-C | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 16d2c7c5-9806-39a7-a989-9c7188b8380c | -18.582199 | -47.292702 | 2024-10-07 01:19:50 | METOP-C | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bf9d4c2f-2b68-3974-a21a-055b3c3cafff | -18.585899 | -47.306801 | 2024-10-07 01:19:50 | METOP-C | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dbf81489-4eb2-3cda-b520-ca54adc6a0c9 | -18.2955 | -47.112 | 2024-10-07 01:19:54 | METOP-C | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 435de494-52b9-3ac7-a053-043f6f15d276 | -18.299299 | -47.126701 | 2024-10-07 01:19:54 | METOP-C | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 367c0c79-d877-3258-a6b9-ec985609ee35 | -20.0746 | -54.524899 | 2024-10-07 01:19:54 | METOP-C | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8d7e6169-b208-37d8-88cc-a5b960772201 | -20.0762 | -54.5322 | 2024-10-07 01:19:54 | METOP-C | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b05040d8-55a8-3d07-9835-e9537ad5e54f | -20.0648 | -54.527199 | 2024-10-07 01:19:54 | METOP-C | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 402f26a6-bf0f-3ad0-a4db-afed912cd0d3 | -20.066401 | -54.5345 | 2024-10-07 01:19:54 | METOP-C | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 641cb2e7-3602-33be-9f5d-37e08c3eb298 | -19.388201 | -51.685299 | 2024-10-07 01:19:55 | METOP-C | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2344b073-7c8b-3b44-b0f5-8747b80d60e1 | -20.213699 | -55.991901 | 2024-10-07 01:19:57 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8a48639b-a040-3a63-a0cd-965e023a13ae | -20.261299 | -56.516399 | 2024-10-07 01:19:58 | METOP-C | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ac7198c9-3ae9-3f45-911f-0ed7f11f88da | -20.263 | -56.524601 | 2024-10-07 01:19:58 | METOP-C | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 167cb5e0-00c5-3b1a-981c-666fa38c11f5 | -19.552999 | -55.0583 | 2024-10-07 01:20:04 | METOP-C | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a1f423ec-80d6-337f-a3b1-d74d7f8900d2 | -19.554501 | -55.065601 | 2024-10-07 01:20:04 | METOP-C | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 40499db5-f685-3b8e-b18f-a124b255ca8b | -17.8941 | -48.604301 | 2024-10-07 01:20:06 | METOP-C | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9aaae631-716d-3fbd-ba0c-28c86d68b146 | -19.6555 | -56.459599 | 2024-10-07 01:20:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6019e13b-4b2d-3c1b-a5f3-a15453062335 | -19.6572 | -56.467701 | 2024-10-07 01:20:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b490fc33-6da8-3c59-9021-f65cfea4add5 | -17.8813 | -48.595001 | 2024-10-07 01:20:07 | METOP-C | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 63da4521-5435-3d0e-90ae-f717899a3a5c | -17.884399 | -48.606998 | 2024-10-07 01:20:07 | METOP-C | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| de5e62f8-5e31-30b3-b98c-9347ba4b3c73 | -19.641001 | -56.488098 | 2024-10-07 01:20:08 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cbb535ae-fdc6-39f1-b431-b6ace6806025 | -18.8883 | -54.466202 | 2024-10-07 01:20:13 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8abebffd-f8eb-38d5-ba5a-a28aa7ab87ba | -18.8899 | -54.4734 | 2024-10-07 01:20:13 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 49f66b7d-cbaf-3459-baf2-d5eb805bef60 | -18.8915 | -54.480701 | 2024-10-07 01:20:13 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5e79b78e-a67f-30c4-94ef-29861dc2d510 | -18.893101 | -54.4879 | 2024-10-07 01:20:13 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d0368dc4-516c-3467-b91b-15947ef39a6b | -18.9011 | -54.523998 | 2024-10-07 01:20:13 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b9f40bbb-8fb1-3568-b2e4-db21dd97bfd9 | -18.9027 | -54.5313 | 2024-10-07 01:20:13 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b19e19ab-0ef3-389b-bb81-1b101faa02b8 | -18.889799 | -54.5191 | 2024-10-07 01:20:13 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3f26fb1d-2bdd-3de3-927b-e320cf70322c | -18.891399 | -54.526402 | 2024-10-07 01:20:13 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 498116b3-6eab-3223-9753-5899e34336c7 | -18.893 | -54.5336 | 2024-10-07 01:20:13 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 25d2c3ef-ec60-3d43-9537-eb34c12395d2 | -18.8946 | -54.540798 | 2024-10-07 01:20:13 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 95ceb5f1-89e1-3c9d-a26e-efc8cdbd31fa | -18.8962 | -54.548 | 2024-10-07 01:20:13 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ecfecc71-f652-3668-a8ea-e9c10f4084d4 | -18.8978 | -54.555302 | 2024-10-07 01:20:13 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c25a2f51-8343-3570-9528-8f20e1df4316 | -18.8864 | -54.550301 | 2024-10-07 01:20:13 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a8d199db-c91f-3a61-aa7e-bf310e41413a | -18.888 | -54.557598 | 2024-10-07 01:20:13 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a370a070-df79-3221-bbbe-bca75a6e6b5b | -18.889601 | -54.5648 | 2024-10-07 01:20:13 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6a13c246-0397-3ca9-99ab-37f8884ebca0 | -18.855801 | -54.458801 | 2024-10-07 01:20:13 | METOP-C | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b065f3b1-3666-3590-9696-c0a50d72ccd4 | -18.875 | -54.545502 | 2024-10-07 01:20:13 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| dab7da1e-2cac-397e-a241-652eb8d9b81f | -18.8766 | -54.5527 | 2024-10-07 01:20:13 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e279e371-6590-398a-b51a-ec8b5222a74c | -18.878201 | -54.560001 | 2024-10-07 01:20:13 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3e0ff0dc-12d0-3cc1-8aed-68a16a5eb3cd | -18.879801 | -54.5672 | 2024-10-07 01:20:13 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 58c2a759-eb8a-3abb-8f35-410f902b8140 | -18.8636 | -54.5406 | 2024-10-07 01:20:14 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3e3ec170-1876-36d8-90ca-6c216524e336 | -18.8652 | -54.547798 | 2024-10-07 01:20:14 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a497ad07-ba86-3246-ae86-9efdd8b61650 | -18.8668 | -54.555099 | 2024-10-07 01:20:14 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 36e0f65e-a709-313c-8139-a2cbf3295523 | -18.868401 | -54.562302 | 2024-10-07 01:20:14 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 270027b2-01ee-37c0-b304-faf8c798c510 | -18.870001 | -54.5695 | 2024-10-07 01:20:14 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ba92ae72-059b-3729-b315-fbb22aa1bf17 | -18.855499 | -54.550201 | 2024-10-07 01:20:14 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 940f1471-44a4-3425-b478-390afaf28ec8 | -18.8571 | -54.5574 | 2024-10-07 01:20:14 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 73b303f0-417d-34fb-9cb5-36aa6748b4c7 | -16.900801 | -47.140499 | 2024-10-07 01:20:16 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dcef25a5-0aa2-3d7c-93cd-9ba3ca32b4ac | -16.891199 | -47.143299 | 2024-10-07 01:20:16 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 76193a04-eca3-3b54-aeb2-b8d2885c5e5d | -16.895201 | -47.158699 | 2024-10-07 01:20:16 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4a0f2142-9e90-3c98-b524-d9d73861ebba | -18.4638 | -53.493 | 2024-10-07 01:20:16 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 82fd1a23-febe-3c07-b9d5-8fa557221757 | -18.4655 | -53.500301 | 2024-10-07 01:20:16 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 45e72f39-74a1-352b-a096-39c3c81f0549 | -18.4671 | -53.507599 | 2024-10-07 01:20:16 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 33796a61-d47b-3577-9821-8f9f0ef6b499 | -18.4688 | -53.5149 | 2024-10-07 01:20:16 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2b45586a-efee-3b7f-9ecf-6a2e6b89af81 | -18.452499 | -53.488098 | 2024-10-07 01:20:16 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 96eaf7b8-e949-3cc1-bba5-5d806732f085 | -18.4541 | -53.495399 | 2024-10-07 01:20:16 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d028c701-f0ba-39d8-9116-a0041e1b4084 | -18.455799 | -53.502701 | 2024-10-07 01:20:16 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a5237426-188a-35f3-8298-9beedaf1c5ba | -18.457399 | -53.509998 | 2024-10-07 01:20:16 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f888ac35-2dce-35f5-8104-9e9750dfac3e | -18.459101 | -53.5173 | 2024-10-07 01:20:16 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8a324607-1edf-3a5a-8e5e-98f1924c2d0a | -16.8815 | -47.146 | 2024-10-07 01:20:17 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 94385119-1c33-3869-bb3e-b170599ad559 | -16.885599 | -47.1614 | 2024-10-07 01:20:17 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 64c2d61a-c640-34dc-9100-6eb03813c7cc | -16.871799 | -47.1488 | 2024-10-07 01:20:17 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f96436e2-6528-3dc7-b5a7-77b43d473f21 | -19.1064 | -57.468399 | 2024-10-07 01:20:20 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1e705b53-11d8-3be6-b178-84bff746565c | -19.108101 | -57.477001 | 2024-10-07 01:20:20 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e6cebe46-5fae-3f18-9bbb-9ffafbb52594 | -18.719601 | -57.2784 | 2024-10-07 01:20:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 63af20ba-82f3-365b-a8e7-e5a38feb70bd | -18.7213 | -57.2868 | 2024-10-07 01:20:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7f2e3d74-a8eb-3f2c-b159-46871ff6e34a | -18.723 | -57.2952 | 2024-10-07 01:20:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a643be60-8cd6-3ff6-9861-33b6ba40a8fc | -18.7029 | -57.247101 | 2024-10-07 01:20:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1c3acc37-7175-3e68-9ccc-c2d3c81532df | -18.704599 | -57.255402 | 2024-10-07 01:20:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| db1e6d72-958d-3740-9f0a-d498c46661aa | -18.706301 | -57.263802 | 2024-10-07 01:20:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5128d206-a698-3328-b495-2ece4a6cfed8 | -18.709801 | -57.280499 | 2024-10-07 01:20:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2a0750db-9cda-3663-bc87-bc048150b486 | -18.7115 | -57.288898 | 2024-10-07 01:20:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| af7965b6-b1cd-3be5-8fe7-d356c162e1bc | -18.6931 | -57.249199 | 2024-10-07 01:20:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8437807a-84f1-3f7a-b24a-0a2b071b6bda | -18.694799 | -57.257599 | 2024-10-07 01:20:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ceda9c4a-a4d8-3b1f-aedd-19287c4dcefb | -18.681499 | -57.243099 | 2024-10-07 01:20:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bffd584c-af42-3c34-bec5-ad608f6f0a2d | -18.6833 | -57.2514 | 2024-10-07 01:20:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d6cba04b-7a5a-3563-b07b-62890283d7b8 | -18.671801 | -57.2453 | 2024-10-07 01:20:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6a075d78-c43a-3f19-aaac-b812d3e278b7 | -18.6735 | -57.253601 | 2024-10-07 01:20:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| eed52707-4043-3248-9bd0-9536a3c42717 | -18.6602 | -57.239101 | 2024-10-07 01:20:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 40e27aca-64e5-364d-8089-300af7eea413 | -18.662001 | -57.247501 | 2024-10-07 01:20:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a3c07c80-87b4-3c19-858c-b55ba360e246 | -18.6488 | -57.233002 | 2024-10-07 01:20:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4c7e0a81-ba7a-3d09-9a79-31fa2105014c | -18.650499 | -57.241299 | 2024-10-07 01:20:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1eb00a0f-5039-313b-9f36-00ade1415ae5 | -18.652201 | -57.249699 | 2024-10-07 01:20:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 238baee8-c36e-3c88-846e-e14303494816 | -17.7721 | -53.0872 | 2024-10-07 01:20:26 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3843f8a5-5898-372e-8779-c589aad0a540 | -18.640699 | -57.243401 | 2024-10-07 01:20:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 012539dc-f58d-3f0d-8286-5c22042da29a | -18.642401 | -57.251801 | 2024-10-07 01:20:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 16909493-66a8-342b-ad1a-8e231d5910bd | -18.630899 | -57.245602 | 2024-10-07 01:20:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6f965459-6a62-329d-94e9-d0d3a04faf79 | -18.632601 | -57.254002 | 2024-10-07 01:20:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 03d71e4a-0e58-367b-b7f9-fb8872f8ab20 | -18.634399 | -57.262299 | 2024-10-07 01:20:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c9f8190b-e524-3a17-aed2-820f409017e8 | -18.6378 | -57.279099 | 2024-10-07 01:20:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8fac4bc4-d4e0-3da9-9733-c9eebabcd575 | -18.6395 | -57.287399 | 2024-10-07 01:20:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b690b879-b856-3af6-9e63-788cad9e3c52 | -17.8356 | -53.7701 | 2024-10-07 01:20:27 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3e3bb6f3-165a-3661-8018-1417cb70c14b | -17.837299 | -53.777401 | 2024-10-07 01:20:27 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 21240fc1-6945-3c85-9a27-f1cebd13790f | -17.8389 | -53.784599 | 2024-10-07 01:20:27 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3336a0a1-1179-3d62-ad1b-0154ca2148f1 | -17.840599 | -53.791901 | 2024-10-07 01:20:27 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 15d30f35-8db5-375b-83bf-d7c6a5c41212 | -17.664101 | -53.066601 | 2024-10-07 01:20:28 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e125ca36-f401-3567-a900-5c2b2158f99c | -17.6572 | -53.036701 | 2024-10-07 01:20:28 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d9f90186-9c71-31de-a3ca-20dd13aac49d | -17.658899 | -53.044201 | 2024-10-07 01:20:28 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README18.md)
