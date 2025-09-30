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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f25a64e-b647-38c9-8075-375710f4ae1f | -15.3795 | -47.08084 | 2025-09-30 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f5861707-6822-33b1-9444-2d961efcc5df | -7.17173 | -41.70388 | 2025-09-30 03:49:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8e7a7a8c-4afe-30c7-920f-d706f49d4b53 | -12.75657 | -46.87402 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 91622556-330e-3c2d-b2dd-f002473136d9 | -15.25653 | -49.72099 | 2025-09-30 03:49:00 | NOAA-20 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42a2e38d-aabe-32d7-98b9-9148db74c4f1 | -12.84053 | -47.00026 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffeb804e-af90-3f94-b20d-dbe781ff4924 | -6.05507 | -42.47878 | 2025-09-30 03:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8c5743ff-94f3-3da2-8d04-cc29b5802f6e | -7.03931 | -46.41999 | 2025-09-30 03:49:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3ccbe5c-1771-312d-ad3d-758582380b3b | -12.74932 | -46.87108 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6da3872d-c1fd-3c3b-a9ee-53b471aa91d7 | -6.81952 | -44.47153 | 2025-09-30 03:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1825ab68-eba6-3ccd-b746-351ea917fb5e | -14.68637 | -48.13893 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 770c8288-42cc-36a9-8219-5e9caed384cd | -14.55572 | -42.48896 | 2025-09-30 03:49:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7e18046d-0e29-356f-aacd-c6f3570583a8 | -12.2172 | -43.7546 | 2025-09-30 03:49:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3791ffd-edd3-38f3-90df-32ceb8489668 | -5.73878 | -42.68428 | 2025-09-30 03:49:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 751b31dd-566d-3066-a03a-5e50d01f6f65 | -6.40841 | -43.75422 | 2025-09-30 03:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 063a7f31-e8e6-3d90-9ea3-ae0d2c478e81 | -12.84764 | -47.01845 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4459170d-4bd7-3932-8dec-1eb50a37eb4b | -12.75715 | -46.87105 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b15b6884-efc3-3da2-8f89-96ad8a1de997 | -12.96412 | -46.86875 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32150a3a-5eca-38de-ac97-df3e9e4ea5c0 | -13.61545 | -48.03556 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1c2cfbcf-90d1-31ba-ba44-5923eaaa395e | -12.22145 | -43.75498 | 2025-09-30 03:49:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3057397e-8bd4-3590-9677-e07ec8764361 | -12.82954 | -47.00194 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e911a3d1-1b09-3832-918f-1ae49a08e2ca | -12.85139 | -46.99922 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a81716c7-80ae-3f92-bd60-a5f4770b8d1d | -6.36826 | -45.64452 | 2025-09-30 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bd0984d8-b8f5-3905-94c1-e537afe07e54 | -15.68595 | -46.2584 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5cafd29-cccb-3e20-98ca-7dcfa6569475 | -12.77582 | -46.85661 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28f9edae-6108-3689-9a4d-0ed723b0fd4e | -13.81263 | -47.49118 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14bc0aa7-18ac-305e-858b-167c5a82175c | -13.06354 | -47.07869 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d8534a8-85fd-3577-840f-0236f2099502 | -13.06481 | -47.07217 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04871e5c-d3df-328a-8ba4-bfe3cffe2be7 | -14.72267 | -45.22609 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a9ca425-8a4e-3781-9223-133e7a76d839 | -5.47994 | -48.66412 | 2025-09-30 03:49:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3c2140dd-fb4f-372b-85dc-bdb090e27d9f | -15.71573 | -47.58088 | 2025-09-30 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 52e26076-77eb-363e-861a-25eb240d4e83 | -14.74852 | -45.66387 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac6297a1-3ce7-352c-9fbd-3dfdb56150d1 | -12.82204 | -47.00318 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 885e8944-679c-3933-98a7-b53d3ac96974 | -13.80482 | -47.97381 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4ee7d8a-7c33-35e8-8562-871c9358a4a8 | -13.36894 | -47.31854 | 2025-09-30 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68f45389-1062-3012-9233-338c16fa213b | -5.81777 | -42.77887 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| ee5f4f1f-39be-38e7-9c45-713284088edb | -14.53367 | -48.24638 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 816c3871-4f41-34f0-8d65-80018fb1f6f7 | -11.06292 | -47.82 | 2025-09-30 03:49:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 02543449-9e2a-310b-bcb0-cce482f8e782 | -13.22415 | -50.93978 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f9ad025d-635e-3e2c-b939-7e1d7f0724f1 | -11.16843 | -47.23769 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33aa52a0-9caf-3908-8267-afee4e7b443b | -6.09026 | -42.66059 | 2025-09-30 03:49:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 45765e51-8788-3c2b-b94e-9d52acc92002 | -17.72872 | -46.67759 | 2025-09-30 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b51faa60-c3ae-3e14-89f3-df7cb906333b | -14.53527 | -48.25726 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 69c67c58-2487-3c22-a570-4610cf5f2392 | -7.01218 | -45.21441 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4de6420-3d8b-3325-ae01-660307e88679 | -12.83996 | -46.99285 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d66b143-0e92-383b-a6be-1dd4abcda25b | -6.27093 | -43.65285 | 2025-09-30 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a18c1236-a200-3b78-9aff-2753d5692c39 | -13.22987 | -43.37016 | 2025-09-30 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 57e80183-b945-31e6-a52d-f56f719fbe66 | -13.62732 | -48.03905 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43cea8f9-a85e-3347-bd15-3845ad498da3 | -13.57687 | -48.06023 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3c7a010a-07ea-3895-945d-423249406f8b | -15.27854 | -39.18552 | 2025-09-30 03:49:00 | NOAA-20 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9992101b-9f52-3b31-b122-6ae54a162d25 | -6.11353 | -43.44567 | 2025-09-30 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d519f2b3-188a-3b7b-9592-52d00d66849d | -5.77823 | -42.85187 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cb78f71d-905f-3535-8a4b-c8c4ee751335 | -12.95985 | -48.41684 | 2025-09-30 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4eb89668-7ed5-3a08-9197-f3c06f39d43d | -13.59274 | -48.03671 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45410291-f80b-3403-aac1-b6011ec8ba98 | -6.37 | -45.63486 | 2025-09-30 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdb26abb-14ab-3a5e-909c-e9f4d345a0ae | -17.47153 | -46.20046 | 2025-09-30 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd210c33-f3bc-35b6-80e5-6ece44dedf59 | -6.39805 | -42.8159 | 2025-09-30 03:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 317f7c0b-af05-338b-b485-9bb47a0e9ae9 | -13.00493 | -49.44358 | 2025-09-30 03:49:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50b42812-ebaa-31c6-b9e2-d032112c814e | -12.94946 | -48.41036 | 2025-09-30 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0745177b-d4e5-3b03-82a9-a1a9a892b779 | -5.74384 | -42.68078 | 2025-09-30 03:49:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3de7cf1b-e8ab-3130-b5e0-d987a6f80817 | -11.89094 | -48.02772 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c7acb96-2156-3f26-8654-bc97229b2a21 | -5.73769 | -42.82394 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4a9d6fd5-a90a-3bcc-8ab4-16c5dda269d1 | -15.27344 | -47.89531 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3274bb04-fbb8-3627-8e27-74161d8df399 | -11.90718 | -48.06313 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a326f7e-f292-33f8-828e-33273df1af1d | -6.65946 | -41.39517 | 2025-09-30 03:49:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 49752069-c25a-3c34-9767-7eb87789e1e0 | -16.60691 | -43.35995 | 2025-09-30 03:49:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2456c85e-4fc0-3ebe-b34e-dcbd29235915 | -12.96549 | -48.41782 | 2025-09-30 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8981d4cb-d435-3194-a69b-2a98eb71e21b | -13.78741 | -47.97701 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 495ea2c7-c6cf-3346-8ecc-8b183b35a349 | -11.88422 | -48.04363 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a60ddc32-c888-30ff-b347-ce113bf0a271 | -13.00886 | -44.11794 | 2025-09-30 03:49:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 527a0514-5627-3678-a598-0ba4bea4af18 | -6.05157 | -42.4798 | 2025-09-30 03:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8e8c6459-0853-337e-84a6-69294eb747ee | -6.14984 | -43.90191 | 2025-09-30 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a3537aa3-2ced-3b26-9a8e-a50cfaf82a56 | -13.59773 | -48.03991 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9a62414-9af0-35b1-b754-daec29066df9 | -14.51652 | -48.44077 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e15a559-b3e8-356f-b021-9eeefa219d61 | -5.71509 | -42.87765 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e806c7be-1942-36b8-a504-be03de9c9159 | -14.54675 | -48.48825 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2c48fc31-b9e6-333c-beec-87c820d1d6fb | -13.78261 | -47.97304 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f917fff0-296a-3196-a440-86be8c7a7f27 | -15.3919 | -44.97455 | 2025-09-30 03:49:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74ec88c0-c984-3d69-bca7-e2d7e809d94f | -12.84954 | -47.00873 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 58e5c425-94eb-3ba2-91bf-b0ced21b123f | -12.95569 | -46.40805 | 2025-09-30 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7249055-ae46-3cec-8b85-a9e8c4e5acbb | -13.65771 | -44.39766 | 2025-09-30 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c349fdc-3406-321b-98fc-7fc019da6cbc | -13.36156 | -47.30107 | 2025-09-30 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f93051cf-1038-394f-b42d-938a7f606be1 | -13.38271 | -48.06486 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac448cb2-cefc-3ed2-9493-04b46275653b | -14.59233 | -48.28975 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6df5ac79-b3dd-3074-9580-8e91f8264bbb | -6.36851 | -45.61396 | 2025-09-30 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aea42126-3d35-359d-a1dc-68d266d3dc5e | -6.28797 | -43.46845 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 98742a96-de7f-31fa-86d7-a6899e4b564c | -14.57219 | -48.2225 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3b46272-d514-3eb2-8f3c-83ce026516f5 | -5.73141 | -43.96944 | 2025-09-30 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e1fc37b6-3abd-3d7b-bfce-59f120121727 | -12.69598 | -45.29504 | 2025-09-30 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0384ee05-42f8-3d0d-b143-c17b299bbdda | -7.29188 | -42.8667 | 2025-09-30 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 23b264cf-095f-3926-8996-c47c5b281a40 | -13.83206 | -47.47514 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c2d624c-a9b3-3336-90f3-5c959b5f4433 | -6.69665 | -44.55409 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6c3d4656-1aa9-309a-8555-3d81bcc8cd23 | -7.01002 | -44.47852 | 2025-09-30 03:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a12a4584-b67f-3878-a4f1-8be80d6f1d78 | -13.81589 | -47.50051 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f9d5613-09b9-3612-aeff-918c8b991c8f | -12.75197 | -46.87049 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6948ce78-a026-3c8a-afb2-53c2351bec11 | -13.62675 | -42.53175 | 2025-09-30 03:49:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3d6e430a-3507-3057-bb3b-bbea81876cc3 | -16.22783 | -41.72793 | 2025-09-30 03:49:00 | NOAA-20 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 235810d6-83c4-3571-bb72-49b0a269a999 | -12.37851 | -43.89885 | 2025-09-30 03:49:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7db987be-99aa-3847-9208-c79cb9b00751 | -5.74312 | -42.68502 | 2025-09-30 03:49:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4fa741be-feac-3193-b297-77c4baa7ef1e | -13.23062 | -50.94127 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3cdb30b-8ad0-3f26-b5c1-8d94126bd1ed | -12.92655 | -47.14183 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README29.md)
