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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56b36735-c3d1-31cb-a945-1ce64d088a6e | -16.73419 | -57.46724 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 565f5d73-71a8-3900-81c5-5d04ef9d3a5a | -16.73068 | -57.4666 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9ab840b2-fdff-3a6c-baa6-80980c1985a4 | -16.72856 | -57.45787 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 0d304b18-5674-32ca-8bd0-bea2207c4dbb | -16.91816 | -57.70092 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c043690d-f2b7-3bc8-9bb0-618986b10535 | -16.91674 | -57.70915 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 49f384fa-0845-3c7c-b747-7f120d55b2c3 | -16.91463 | -57.70026 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7642c4f2-9f79-32d1-bcc2-3ff686f2f60d | -16.90332 | -57.70242 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 597f2379-130a-300a-a389-468b63e26890 | -16.88924 | -57.68439 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f7b2c74b-d8f0-3d1c-ad2d-fa843e94777f | -16.87372 | -57.69 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| beeb190f-d58b-3a88-9518-dae666c5c2a1 | -16.87163 | -57.70235 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3d3fda7a-e959-34be-bcfd-4cd4fbf89a5d | -16.83171 | -57.46785 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| babb6c99-5b9b-3ec6-9d49-633b1e8c7885 | -16.83102 | -57.47188 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| abcdcff9-1c5a-3d37-bedb-6eb8532d09e3 | -16.8289 | -57.46317 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5185356a-5caf-38a5-88d5-80013dff224a | -16.82821 | -57.4672 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c6489da3-c069-364b-93af-d2f4b3cd92f2 | -16.82752 | -57.47124 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| dd0b9711-4ebc-3449-b7a3-2701805fe7c9 | -16.82471 | -57.46656 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4a80bb31-4ff8-3427-ac11-bc743dce65bc | -16.8212 | -57.46592 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 41f2a068-965d-39e1-aed2-68ee5f7c8c3b | -16.82104 | -57.46653 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 66a02bac-8011-3e78-94fb-7664c15ad8ce | -16.81853 | -57.56579 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 329f544d-cdf5-356d-8266-a0b10c2fafe6 | -16.81631 | -57.47336 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 076d3cc8-e77c-3dd1-a8e4-7251efa3f4cc | -16.81571 | -57.56107 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c553d7b3-8064-3187-9519-3dc6cc982d54 | -16.81501 | -57.56514 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 4690ad0f-a494-3bf9-b809-af72af71d506 | -16.81149 | -57.5645 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 46e82ec6-3ef3-3612-a37e-6fd704fd87e9 | -16.80443 | -57.37218 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8bf87c9a-6334-3408-a13d-65453b334e8d | -16.80375 | -57.37619 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b16e7deb-2173-3bfd-97f8-5091896d007f | -16.80217 | -57.47138 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| a836fba9-d119-390e-a69d-f7400ea84e50 | -16.80026 | -57.37555 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 24944d28-285b-38b5-9342-2d762b10daed | -16.7974 | -57.64622 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0e1943de-68f9-38e5-aff5-7fc7981507b4 | -16.79387 | -57.64557 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| be9d6198-6803-38d1-af00-39c92b8cd259 | -16.78405 | -57.49309 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2eaf8a67-f2e9-381b-9665-fa5eb76dbf5a | -16.78337 | -57.49714 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 13834157-c140-374d-a8f6-70513dc20774 | -16.78191 | -57.48434 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| dab7d35e-f091-32f9-88fc-7e4b9069ed33 | -16.77677 | -57.42927 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| f9f697f0-a286-3e6f-a56c-6aba03c07de2 | -16.77609 | -57.4333 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 37638f15-af49-3115-8749-64886cbb9b8a | -16.77426 | -57.33776 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f22a481c-a881-3347-a8da-54402aef44e7 | -16.77412 | -57.46624 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 5cd56150-dc4f-3998-981f-316569535524 | -16.77327 | -57.42863 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 1a68b556-2a0b-3423-936a-b3141e5ce7f8 | -19.10883 | -57.49331 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d0725b26-fb5b-344d-82db-146e6249fa48 | -19.10816 | -57.49727 | 2024-10-03 04:53:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3fbfceaa-ee4b-3689-848d-fafdd7d681a1 | -19.10729 | -57.48145 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1492ef8a-5854-3872-8e23-8babe6383db2 | -19.10667 | -57.48513 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4b401dba-f90e-318b-ae22-142784ede3df | -19.10604 | -57.48888 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6308def7-dcff-3528-8eaa-9c11e79d895c | -19.10538 | -57.49276 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| eecf9f42-481c-37ca-a48d-5be41839223a | -19.1026 | -57.48827 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 81e9dd8e-89fa-347d-adee-0540b02f958e | -18.72727 | -57.33089 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 595c0481-7707-3275-8b84-72b9e48db665 | -18.72384 | -57.33027 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4a5f4a8d-8d88-3169-be39-119b3cb0576f | -18.72319 | -57.33416 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 94df630f-11df-34f1-a2e1-2e7c179b8d1a | -18.72122 | -57.34587 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 531fa011-3c7e-30ae-8473-fa4400b5e922 | -18.72041 | -57.32964 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b98b0479-01fe-3c66-8fab-be8a4d9ab432 | -18.71976 | -57.33354 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c4a57ed6-7748-3e13-9df0-b4a4afc6fde0 | -18.71829 | -57.32122 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| edb1141b-28ae-3ca1-968b-e8888ed083cf | -18.71764 | -57.32511 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 217817e4-fea1-3adc-b73d-997391e643f1 | -18.6997 | -57.30574 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 97ea8221-b8e0-37f2-b2fd-da017e4f820b | -18.69904 | -57.30963 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e6915df4-9648-32fa-892e-96d82a601762 | -18.69627 | -57.30511 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c9090d21-90a9-32c3-97a9-d132867d78c1 | -18.69562 | -57.30899 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d02a965a-e6df-34fb-b73e-a023f5ec0161 | -18.69496 | -57.31289 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 63b5552f-6db1-3da4-b158-ff1991ae9ea8 | -18.6943 | -57.31678 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| def59b20-10f7-32e4-9d99-e2d010ee6097 | -18.69219 | -57.30837 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 64056feb-dbd8-3b3e-be4a-16247d5b5ce3 | -18.69153 | -57.31225 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 54ea63b1-b3d7-363d-8c92-f972a3c30378 | -18.69 | -57.3085 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 338f0cdd-fad9-3f41-b586-a8ca65dd10ab | -18.9049 | -57.71167 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 36e3a3f1-a42e-3dac-b460-6c986f74ef9e | -16.60219 | -58.22995 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d89fa762-2889-308a-9692-5086193353c4 | -16.60159 | -58.21193 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 69abc27c-94a4-3fdd-8aed-f2ac4d18ddaa | -16.60083 | -58.21625 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 56b7a46c-4e60-3276-9d66-6d2b2506ce68 | -16.60008 | -58.22057 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c36782ca-1b05-35ca-9158-4326139a1d49 | -16.59932 | -58.22491 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cbeab7f9-32d0-345c-8be4-2f51c8d0f556 | -16.59855 | -58.22927 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ce8c45e2-55b4-3652-a4d6-331707141a83 | -16.59779 | -58.23365 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 46b2de73-ec80-36b1-ab3a-0b37439177f8 | -16.59721 | -58.21557 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b48c4db7-5172-3ce0-b027-469f501aba5b | -16.59645 | -58.21989 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 25c188ea-6ef4-3245-bc0d-66637463ebaa | -16.59568 | -58.22424 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7d830b13-c598-3446-8c1e-69e16ffb3371 | -16.59492 | -58.2286 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 28d408db-86fe-3d6d-84c1-03b7b6d6a8f1 | -16.59415 | -58.23297 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| cfff59d0-b060-36aa-8402-b98f2751ffa9 | -16.59358 | -58.21489 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2c73fecf-9516-37d2-b3b3-e887ea772594 | -16.59338 | -58.23735 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c712c003-9190-3a60-9676-6c555c0081c1 | -16.59282 | -58.21922 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e8fe080f-3244-3ede-9eee-22934b4d98e8 | -16.59261 | -58.24175 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a0fe4004-761b-309e-b68a-b7016467229e | -16.59129 | -58.22792 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7aeab7dc-cf83-3376-b33d-84d34f2a2427 | -16.59052 | -58.2323 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c365a229-8871-3962-918f-9dcf39df42ad | -16.58975 | -58.23669 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| b53b516a-b625-3ff1-bbac-f3b1d24d11c1 | -16.58897 | -58.24109 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 20e968c8-708c-3eef-8759-bc413c083710 | -16.58534 | -58.24042 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 79cb1965-a79e-3e10-b427-ea3b082443e1 | -16.56807 | -58.23486 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 88fb260b-7766-36d6-9473-52aa5b1e687c | -16.56518 | -58.22982 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 712969d7-940e-3c3e-88e8-61b25d969fcc | -16.56444 | -58.23418 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 1acdba7a-016d-3d15-890f-c81463178b2d | -16.55867 | -58.2241 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| b363c829-8be2-303c-883a-8848e4c5e784 | -16.55653 | -58.21469 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 65be3311-4791-39f1-b2b7-08a26ecd067e | -16.55578 | -58.21904 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 33394938-bf10-35aa-ad89-6559e1c5c686 | -16.55503 | -58.22341 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.4 |
| 97c4224b-c329-3a64-adf0-41a37ff0164a | -22.66635 | -42.5182 | 2024-10-03 04:55:00 | NPP-375D | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7351d65b-c453-3939-bd74-6cc4ed142ccf | -22.65001 | -43.70063 | 2024-10-03 04:55:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6f91dd3a-acf1-352e-818e-d8ab4180c7da | -22.64958 | -43.70626 | 2024-10-03 04:55:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 21caa3ee-3e08-307a-bf9a-c3152c070998 | -22.64884 | -43.70014 | 2024-10-03 04:55:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 67ee93d7-d655-3303-aa22-200d34a491f1 | -22.64837 | -43.70576 | 2024-10-03 04:55:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 736f4445-6a47-3c4c-b4fa-080034d5a96e | -22.6479 | -43.71147 | 2024-10-03 04:55:00 | NPP-375D | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 513bd6a3-12da-3790-9554-cd205b82c32f | -22.64359 | -43.69996 | 2024-10-03 04:55:00 | NPP-375D | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 01c499f0-21e8-3de8-bac2-d4ac3acec2b9 | -22.64317 | -43.70558 | 2024-10-03 04:55:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| a4ebbdf4-46c7-3ec8-a896-747e811edf50 | -22.64195 | -43.70516 | 2024-10-03 04:55:00 | NPP-375D | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5505b5de-4c75-320d-bebd-2cdf43a63a28 | -22.77052 | -44.66579 | 2024-10-03 04:55:00 | NPP-375D | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |


[Clique aqui para ver as próximas entradas](README148.md)
