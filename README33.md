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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 021d25ab-80b3-3f76-9dfa-e7c7998c82e3 | -16.9249 | -55.8326 | 2024-10-04 01:27:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d67fd28e-deee-3ba0-882b-3596d8499167 | -16.908199 | -55.806301 | 2024-10-04 01:27:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e3053e9e-f528-3585-b714-f1f431f4f622 | -16.9105 | -55.815899 | 2024-10-04 01:27:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a404ba91-9771-3ff3-959d-635686f44e6f | -16.9128 | -55.8255 | 2024-10-04 01:27:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3a41255a-42a5-3c81-92b9-8075dbe39909 | -16.915199 | -55.835098 | 2024-10-04 01:27:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e9d79065-1ee0-3564-8001-461284690219 | -16.9175 | -55.844601 | 2024-10-04 01:27:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 20f2b5d1-4d7f-33b7-96e9-5e89694a0ee9 | -17.121901 | -56.7425 | 2024-10-04 01:27:47 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9260eea9-58d4-3ebb-ba07-1f23dd043d48 | -17.123899 | -56.751099 | 2024-10-04 01:27:47 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c5246d94-42d2-391c-b08a-9426fa318553 | -16.898001 | -55.849701 | 2024-10-04 01:27:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c1b3a94b-a88e-3607-bec6-321799e540f5 | -16.900299 | -55.859299 | 2024-10-04 01:27:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1c72c4c2-2092-3c6a-b7aa-d8d8dd9f2718 | -17.1101 | -56.736301 | 2024-10-04 01:27:47 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eebc0ba9-6f22-310e-bd15-0e07da4a91d8 | -17.1122 | -56.7449 | 2024-10-04 01:27:47 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 41a2be01-873a-325f-8d30-7ed3f3a6986e | -16.886 | -55.842701 | 2024-10-04 01:27:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cf8eea87-d682-3658-b152-756f5579b812 | -16.8883 | -55.852299 | 2024-10-04 01:27:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 919e9ad6-b404-3c05-a657-86e8c620dd54 | -17.1064 | -56.764599 | 2024-10-04 01:27:47 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e2ff47ce-77e7-3262-8814-ddbbd2436b17 | -17.1084 | -56.773102 | 2024-10-04 01:27:47 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 95d36027-ba91-3248-b579-4b6f62394160 | -17.1105 | -56.7817 | 2024-10-04 01:27:47 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f47e7d10-1263-3e17-9e0f-c0f69ce31ee6 | -14.776 | -48.013699 | 2024-10-04 01:27:48 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 19dc309a-6845-3796-80de-fc24f1cad240 | -14.7667 | -47.980999 | 2024-10-04 01:27:48 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dfb5849b-b15c-30f8-a483-51ac210a68c7 | -14.7572 | -47.983898 | 2024-10-04 01:27:48 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b0a899cb-3d91-32a9-8039-ce325483d38d | -14.7665 | -48.016602 | 2024-10-04 01:27:48 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2787b378-0b8f-3fee-bfe8-a1a52d1aab76 | -17.096701 | -56.767101 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3285defa-cfa2-3705-9514-8c95242d8c4a | -17.0987 | -56.7756 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 16fc5311-5f02-3647-a9ab-d17d658342c3 | -17.1008 | -56.784199 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f2c7af09-cbdb-373c-92de-d6a75debbe31 | -17.086901 | -56.7696 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c16dac7e-9ca1-33f5-9506-0c7f49aae676 | -17.0889 | -56.778099 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b107d883-d130-3bdb-8e22-4ceeafc25358 | -17.091 | -56.786701 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 066e5646-09a4-32db-b0f8-2ece23b0576e | -17.054701 | -56.677299 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4bc50c96-fe3f-3b81-883c-c7522ac53769 | -17.077101 | -56.772099 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 712c957d-f73f-3472-8a8d-2f7014ab511a | -17.079201 | -56.780602 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 759b466c-c74f-3025-a84d-7b9a5ffaddf8 | -17.045 | -56.679798 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 64228199-4bda-3a14-b666-483db323d668 | -17.047001 | -56.688499 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6f7715c1-f6dc-3b29-8760-130ce302ba1a | -17.0674 | -56.774601 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 67da5003-1f0b-3f5c-a21d-a75b2fd839bc | -17.069401 | -56.7831 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0e7b49f1-8bea-38ad-ad45-119e7fa2d33b | -17.0352 | -56.682301 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7b0e70db-0bad-33aa-8b0a-f91d8c7aec1f | -17.0373 | -56.691002 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 44abd29d-26ba-3b70-a504-3a7f6949aa2a | -17.039301 | -56.6996 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 197caa59-4575-3e93-90b4-f650177de16c | -17.0597 | -56.785599 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 011c4792-749c-321b-a757-aaeb54b82a03 | -17.061701 | -56.794201 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ae7062d8-a23c-350f-ab8b-98ec3d9b0a44 | -17.192499 | -57.351002 | 2024-10-04 01:27:48 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c75205ae-b887-3fe2-b29e-b70ac50aa29c | -17.025499 | -56.684799 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| da09addd-b33e-3c51-91d3-45d004352312 | -17.0275 | -56.693501 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d3111def-299c-309f-a65c-e2684d53e07d | -17.0296 | -56.702099 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 03af4d63-cc67-3353-8696-335323df72be | -17.031601 | -56.710701 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 79c8f960-a73c-3d33-886b-ad793ae28cd7 | -17.0459 | -56.771 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3e602053-cda4-35cd-94d6-1c8eb063b527 | -17.047899 | -56.779598 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 533de685-1ad4-345e-84f2-df04a723eb54 | -17.0499 | -56.788101 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b35cda5e-97c6-38db-9b93-cd76027a5806 | -17.052 | -56.7967 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 412e746c-72d0-35c1-b67e-4bab1ae79fcb | -17.180901 | -57.345402 | 2024-10-04 01:27:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4428e67c-ef19-3174-aace-8f1de44d1908 | -17.1828 | -57.3535 | 2024-10-04 01:27:48 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5aa95494-1810-3ad5-a8b8-2d00f6e04547 | -17.1847 | -57.361599 | 2024-10-04 01:27:48 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e44e794c-c664-3a0a-908e-5a8c4f166d7d | -14.7477 | -47.986801 | 2024-10-04 01:27:49 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bcc38c55-6cce-30fd-bbfe-a2d7a277002d | -14.757 | -48.019402 | 2024-10-04 01:27:49 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6e7f6b40-f3d2-3ce3-b506-d6e8df51406f | -17.0259 | -56.730499 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4cd554e1-bd05-35e0-91ae-0b794f214de2 | -17.028 | -56.739101 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7d9b86aa-2726-3d29-b521-8f6c8a579434 | -17.030001 | -56.7477 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b95c22f9-c29a-331a-af00-4c3ac3c8dbb1 | -17.032 | -56.756302 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bfeb5558-16a1-3a2c-a6ae-d9f7c8de28ec | -17.0341 | -56.7649 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 279e1b59-a7b3-3386-b21d-5993e61767fc | -17.0361 | -56.773499 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5d244482-fb4e-320c-a79c-91d7f8c83b60 | -17.038099 | -56.782101 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ed886086-4f1b-38b6-9d3a-6098606c2e72 | -17.040199 | -56.7906 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 027266ab-1f10-33cf-bd38-2429b20d5504 | -17.171101 | -57.3479 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 321bb6de-b47b-306a-b87a-c9eff10a0dae | -17.173 | -57.355999 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a0123912-33aa-3b68-9158-7b321941468b | -17.1749 | -57.364101 | 2024-10-04 01:27:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 675dfb95-759b-3f15-bb0d-69132e96b6aa | -16.7103 | -55.4604 | 2024-10-04 01:27:49 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5244adf6-6602-35a8-9902-81048a215959 | -17.016199 | -56.733002 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 102062d6-e1f7-3e48-84d3-3da8575728a1 | -17.0182 | -56.7416 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 484eb932-cb87-3cd7-9ba4-ee23aea1a17e | -17.0203 | -56.750198 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b963596e-3116-3aef-acd8-b00ff4f61785 | -17.022301 | -56.758801 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f900f164-09ca-39cd-8b5b-797b11c76686 | -17.024401 | -56.767399 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b542a3dd-7916-3a41-8f01-c14d779f64e5 | -17.0264 | -56.776001 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bf3b3a5b-299f-373f-bac0-654ead5acb2d | -17.0284 | -56.784599 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aa612822-2fa7-3582-b15e-fc7535128637 | -17.1632 | -57.358398 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bad9f330-3952-3a93-89aa-17160566c3d1 | -17.1651 | -57.366501 | 2024-10-04 01:27:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d014796b-b22f-3375-82c5-b122f319898c | -17.167 | -57.374599 | 2024-10-04 01:27:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d377643f-5e96-30bc-b77d-fe32a2d84e4a | -17.1689 | -57.382599 | 2024-10-04 01:27:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 84234909-c15a-3b06-8edd-52f9f26f4ffb | -17.170799 | -57.390701 | 2024-10-04 01:27:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2f6b7340-02e3-39c8-ad72-32c644c0d9cb | -17.1726 | -57.3988 | 2024-10-04 01:27:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aa52b17f-f798-3be5-8a7c-8b6c5a12ebbc | -16.698099 | -55.4529 | 2024-10-04 01:27:49 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6cdb9228-8f09-32a0-aefb-7d4ee541971a | -16.7006 | -55.463001 | 2024-10-04 01:27:49 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a4196246-d412-34ca-a23a-f6b090970747 | -17.0044 | -56.726799 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1dc07127-2c1b-3660-a79c-4efe4bedcea0 | -17.006399 | -56.735401 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| caa58e6e-50bf-31c9-b0b7-9dd45c468c09 | -17.008499 | -56.743999 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5426cf9b-f90f-3a5c-8fca-bc3bb4d85e7c | -17.0105 | -56.752602 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bb67e33e-e9ad-3cd6-9516-c1a6904daf51 | -17.012501 | -56.7612 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0daea19c-47ce-3f23-9de2-413f596bc269 | -17.014601 | -56.769798 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fa47bedf-4e95-342f-9371-dffc6caee9fc | -17.0166 | -56.7784 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fd940d30-6000-34a6-a726-d95960821967 | -17.1516 | -57.352798 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d53ed3dd-a1de-3533-b892-ed9159e90131 | -17.1535 | -57.360901 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| db35c2d9-528d-31a9-ac1a-9394f17dc9af | -17.155399 | -57.368999 | 2024-10-04 01:27:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b626b161-4c8e-32c1-9161-50a6d9be87fc | -17.157301 | -57.377102 | 2024-10-04 01:27:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8dc03e3d-1d81-3f8a-bd04-5f0b58df3773 | -17.159201 | -57.385101 | 2024-10-04 01:27:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2cc0085d-a1e6-3d1e-b324-31a8ac402033 | -17.1611 | -57.3932 | 2024-10-04 01:27:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e16f64c6-8e21-3bd8-aeb8-eda46baf3b68 | -17.162901 | -57.401299 | 2024-10-04 01:27:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1134e788-e467-39af-877b-eaeea504678c | -16.6884 | -55.455399 | 2024-10-04 01:27:49 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 33107bf4-e8f6-3fd1-b7d4-6434cfcd7a8a | -16.994699 | -56.729301 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1eb6d1c3-7ce2-3c41-9ca6-f17f0974d087 | -16.9967 | -56.7379 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2a351d2f-c4f2-3364-a203-b788d05b2c03 | -16.9988 | -56.746498 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 70dcb58f-8bd5-3db5-91fb-7a5b73c353a1 | -17.000799 | -56.7551 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1082a1e4-0f30-3c6e-b8e4-5f7c1813bd85 | -17.0028 | -56.763699 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README34.md)
