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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 634d65d3-3cda-3048-bac7-7d198f2a561f | -3.6789 | -49.02631 | 2025-09-05 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2588ca5f-80c7-32d7-8941-693dab378e60 | -4.89794 | -55.84855 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dc68c9c-ff1b-3c67-85f1-a43c594da5bf | -2.43407 | -57.76698 | 2025-09-05 04:55:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d963180e-7628-3a5e-98f1-5aa8e91dda1f | -5.54098 | -43.07594 | 2025-09-05 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 202a8a9d-08d8-3eb7-a42f-b7577f426d78 | -3.99336 | -47.37061 | 2025-09-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a53bba2-e7d1-3fc5-bff7-2b876de041bd | -6.89951 | -45.19154 | 2025-09-05 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a172441-078d-329b-b628-fb1e5d1672f6 | -3.48972 | -48.95244 | 2025-09-05 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9786996-8c24-3ad6-b456-dfe8b83deb2d | -6.23242 | -46.2508 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7e06936-8071-3f01-b8ff-971ea585bba8 | -6.0192 | -46.70071 | 2025-09-05 04:55:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9f2f2439-2f9a-398f-bc92-3443290983e4 | -6.05446 | -46.00166 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecbd4946-743d-3a25-bfb5-16fb925bac99 | -6.90147 | -45.19082 | 2025-09-05 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe83f0d7-98ed-3a32-9874-b9ec3050eb71 | -6.89511 | -45.18375 | 2025-09-05 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77233759-100b-3b8b-9f46-2e55cf51bcf8 | -4.99784 | -56.25549 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de110688-c2ee-30c3-9484-882197c1c739 | -5.94181 | -43.02201 | 2025-09-05 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9da1fad0-16dd-351f-952e-ddf31477108b | -4.97866 | -56.13107 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b36b88c8-aeb8-31ee-9983-eef35adcdd3a | -5.04065 | -56.11359 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11afee98-f3bf-31f4-a2f2-de1e958e7bd6 | -5.70735 | -51.68208 | 2025-09-05 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ec20764-6734-3ef1-86d3-476cc0d787e5 | -5.87887 | -45.57413 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 649d429a-61e6-3954-85cd-f2f2c62c18bb | -5.43305 | -42.85991 | 2025-09-05 04:55:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0a8eade5-f3e3-3f71-a2ad-ded18caf6131 | -6.54347 | -43.91059 | 2025-09-05 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66f1f1bf-0b25-3ac9-aa74-3e0d1a2244c0 | -6.24107 | -42.43524 | 2025-09-05 04:55:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f7da9b8e-68e9-3fac-a132-a5c679e6a38f | -6.25722 | -43.28065 | 2025-09-05 04:55:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8954866d-0ed5-329c-b24d-5a306b457f7b | -2.94292 | -49.01547 | 2025-09-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca178faa-22d1-30e9-b8d2-602ccbac7d1f | -5.60238 | -45.02423 | 2025-09-05 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c93b45ce-6bdf-3efd-af4d-a9d1aef5b18b | -5.10731 | -56.13992 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 730c7a71-0f03-307d-924f-c25faaf8324c | -6.91067 | -45.18963 | 2025-09-05 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4830ffda-0b54-371d-89c4-fcebd32f62c7 | -6.17714 | -47.28655 | 2025-09-05 04:55:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad0fd60d-39f7-38de-8ca3-cbe4c138099d | -6.15837 | -43.18254 | 2025-09-05 04:55:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1c903007-49ae-3385-a0e3-f3e721b092bb | -5.04168 | -56.11405 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6c146b4-3714-3734-8078-fe46fea59a5a | -6.21807 | -43.56476 | 2025-09-05 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5932883c-3dd3-31bb-9226-f4e0e6109092 | -4.20782 | -50.4448 | 2025-09-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 26997bed-e609-39ae-98c3-2bd777bd8dbd | -6.21277 | -43.55961 | 2025-09-05 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40d42c73-6f1f-3348-9a3d-2ea441a96727 | -4.93589 | -55.80904 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d239c17e-3325-3748-90b0-ad474eecd701 | -4.27504 | -48.18815 | 2025-09-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2cd9e1c-0a51-3355-8f3c-994ad5e6072e | -2.50895 | -51.82019 | 2025-09-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8454202f-629f-308f-81db-eef7db1abb4c | -6.5493 | -43.91112 | 2025-09-05 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9bae50ba-05c4-36f7-ae8c-3a07ae4e4782 | -6.01016 | -46.66258 | 2025-09-05 04:55:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 159125b3-1506-329e-8e72-cd1ffead929d | -6.25263 | -46.11874 | 2025-09-05 04:55:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3ea874c-1e5b-3b80-b6e7-10cb499e6223 | -5.93505 | -43.02588 | 2025-09-05 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3aa00fe1-3829-3f43-b009-f7bd03df14c2 | -3.81061 | -48.95131 | 2025-09-05 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e311549a-495c-3c85-8f2d-c2127b8a6a7b | -6.5119 | -43.50467 | 2025-09-05 04:55:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 119472ba-1d90-30ab-a9a3-ffb5b7a6b7b4 | -6.25665 | -43.28478 | 2025-09-05 04:55:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9bef4acb-58ee-38e6-8432-576ccac05345 | -3.85488 | -48.97866 | 2025-09-05 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d94e602-3d08-3ecc-97b3-56241dfe1dae | -5.1986 | -43.69405 | 2025-09-05 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e7b1aaa-d0a7-329e-b8c5-2f87d333cd75 | -5.10507 | -56.13177 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2772b2f8-1207-330d-a003-a62d58be546e | -7.08173 | -43.8707 | 2025-09-05 04:55:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ff43b09-d01e-36af-957d-41d75070fa63 | -6.02821 | -43.69735 | 2025-09-05 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0b52029-b0f4-34ae-a80c-0e63ae3f4d8e | -6.04449 | -46.00013 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 322ecf42-ce3c-31fe-b80d-fd3eaeef5b45 | -6.42156 | -44.01554 | 2025-09-05 04:55:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8256485-e529-3d65-a1a0-17cd7206ba17 | -6.66969 | -48.4045 | 2025-09-05 04:55:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9380b49e-f8fe-344b-b739-8bd34cadede3 | -4.27143 | -48.18371 | 2025-09-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d50c90f8-1042-3bac-89f8-a93a0ceac215 | -5.43445 | -42.85323 | 2025-09-05 04:55:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3a358343-ee70-3ae3-9586-0b93a2005054 | -5.60331 | -45.01776 | 2025-09-05 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 33c955c4-4d84-3dc2-8a75-02e4955a1f6e | -5.43369 | -42.85549 | 2025-09-05 04:55:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 823dc8ed-5d14-33cf-84f0-91a54460de21 | -5.73135 | -49.28878 | 2025-09-05 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4e3da689-6005-3b03-91a3-afa47f7bd093 | -6.67131 | -48.39312 | 2025-09-05 04:55:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c33086ea-b834-3dc6-bba8-f84657db004a | -5.31047 | -55.85683 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 16549f51-4d49-3b14-a875-f231a0399470 | -5.73062 | -45.36536 | 2025-09-05 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 99f184ec-cc71-3edf-9497-3898851232a7 | -5.54762 | -43.07241 | 2025-09-05 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f80de07f-ec69-3df8-b94f-b3bf7fc2949c | -3.44397 | -54.63728 | 2025-09-05 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7133f9c4-158d-37d0-80fd-0a37bb54ad33 | -3.82553 | -51.19478 | 2025-09-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d1a5d71-4e84-38a2-a52e-03ff18abe7d2 | -3.32573 | -54.91329 | 2025-09-05 04:55:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ade8883-8485-3056-8a87-41e32e6e50c8 | -2.47125 | -47.77038 | 2025-09-05 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a51bce4e-bd88-3ab0-bf07-b67503dd7943 | -2.55502 | -47.72807 | 2025-09-05 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3efcf036-aedd-3aee-a8ba-02db294b6804 | -5.10325 | -56.14316 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1688af9e-2a97-3054-b21a-62fe84cba9b3 | -5.60816 | -45.02175 | 2025-09-05 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 675bede1-6dd1-3f11-bebd-bf8a84532bff | -5.53417 | -50.89358 | 2025-09-05 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25175948-2f4b-323d-8971-b1406b767e42 | -6.21336 | -43.55536 | 2025-09-05 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1913285-e864-370b-b150-01953d3d4eb2 | -5.37615 | -45.10742 | 2025-09-05 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7a124b6-9f3d-38e3-9f6d-8b3c87a0f132 | -5.93645 | -43.02464 | 2025-09-05 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 19ff3964-0bba-3c42-a410-add2708b4dcd | -7.08116 | -43.87484 | 2025-09-05 04:55:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acc19bf2-ac7b-3260-b098-cb20a06d88e7 | -5.96914 | -44.7443 | 2025-09-05 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f45bd6c-2092-3751-b86b-7a7757e145df | -5.09572 | -56.14582 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ba63faa-83a7-33ba-92b6-86747a8be1eb | -6.22945 | -42.45029 | 2025-09-05 04:55:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1d5391ab-d729-34fb-b5dd-04c8b70d355d | -7.21553 | -44.18903 | 2025-09-05 04:55:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9dc87da4-3e25-32ef-a03e-004eef744354 | -3.68971 | -49.56983 | 2025-09-05 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c1a6a7a3-8cf1-33a3-8e38-822b05fcec4c | -6.1208 | -42.95314 | 2025-09-05 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f02774ac-e7b6-3e4c-8939-c687d57a9cdb | -6.12017 | -42.95766 | 2025-09-05 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3484a9b8-4a81-32ca-9b80-a4076a0b74d6 | -6.91113 | -45.1862 | 2025-09-05 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d99748d4-428c-3c6f-b547-12da89c6df2e | -3.90165 | -54.68761 | 2025-09-05 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b45b26e0-452a-372b-aa3b-b15a42f66873 | -5.85951 | -46.11333 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a1561c0-6cf6-3f17-99a9-3862a5ef8604 | -5.94863 | -43.02615 | 2025-09-05 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 53e9694f-148e-3469-ac1e-25808912ded7 | -5.10853 | -56.13232 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5285c997-5ad9-32e4-8b65-0f21ba712104 | -5.7801 | -45.27899 | 2025-09-05 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a203e629-b353-3e9e-90eb-d7dea26d1c3e | -3.32966 | -54.91026 | 2025-09-05 04:55:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d88c143a-fc5c-3325-8a99-2254df32c718 | -2.78403 | -49.61819 | 2025-09-05 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 607f8b08-7816-3308-95da-6ac41adc6fd8 | -6.27332 | -43.49958 | 2025-09-05 04:55:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbab13fb-247f-3211-9d59-389327e7694e | -5.01436 | -48.47154 | 2025-09-05 04:55:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 44a90c54-8242-334f-8e26-6e6236093496 | -3.48435 | -52.96319 | 2025-09-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7817e0a5-e7a2-3838-b922-d453b749b71c | -2.38095 | -47.62418 | 2025-09-05 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6976bb0e-b12a-3b62-be78-9f93e8b46094 | -3.15885 | -48.60444 | 2025-09-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcb83479-226d-31f4-98bc-cdfb92205750 | -6.22942 | -42.61632 | 2025-09-05 04:55:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d6545186-4155-3e06-aad2-c931dab9b8c7 | -2.7995 | -48.64389 | 2025-09-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37732a02-4725-3a10-923a-4e18837fee10 | -6.55135 | -43.72624 | 2025-09-05 04:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22c5ec09-3e83-3383-970d-4479b719d9c6 | -6.25066 | -43.28387 | 2025-09-05 04:55:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| abb2ee1c-dbf8-3b20-98db-303124053eb7 | -4.91115 | -47.39355 | 2025-09-05 04:55:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a3c5bef7-7791-36d8-975e-bd6011d6114f | -6.59733 | -44.55701 | 2025-09-05 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f9d97b2b-2b7f-39df-adb9-b44cb4c77157 | -5.65178 | -51.26861 | 2025-09-05 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52273680-001e-3aa6-9c83-065967992d46 | -5.03475 | -49.75791 | 2025-09-05 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3122680-4da3-3745-94f2-13b03e4f8929 | -5.21145 | -43.69378 | 2025-09-05 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README42.md)
