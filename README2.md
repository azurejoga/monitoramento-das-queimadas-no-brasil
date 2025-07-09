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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3955939-6875-3300-82b8-809c8ea4819d | -6.1608 | -48.0289 | 2025-07-09 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 6c27124a-9c68-382b-8c47-61b63e1982a3 | -6.1606 | -48.0507 | 2025-07-09 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 1af25448-fffd-31ec-84ce-ede9c802abef | -8.5028 | -43.2614 | 2025-07-09 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| d8bd21b0-3261-3c4b-9ef4-77512b590b52 | -18.6467 | -55.7351 | 2025-07-09 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.8 |
| 5d1cc2a1-ee8c-3ae6-8317-d67e5d91ad54 | -8.5217 | -43.2593 | 2025-07-09 00:10:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 4733489b-a6e5-3ab6-b2f6-2b14185badd6 | -11.4397 | -45.0923 | 2025-07-09 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 170.7 |
| cd7faf5e-6b68-3100-a5ff-d17f65880c2c | -5.2328 | -45.2102 | 2025-07-09 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 140.7 |
| bd34bcb9-a580-3133-a444-752ce08afae3 | -8.5214 | -43.2828 | 2025-07-09 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 362.3 |
| d5eb1fcf-4c9a-3212-87bb-60db7128dbfb | -5.2328 | -45.2102 | 2025-07-09 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 265b5a8f-68c9-34ce-8d37-0eb12d8f8ac3 | -8.5022 | -43.3085 | 2025-07-09 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| 4c5dc3ae-f82c-3058-9da1-3821c7809f03 | -8.5217 | -43.2593 | 2025-07-09 00:20:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 63.8 |
| 6701bf8c-5dc1-3fc4-a565-6e97ae49edf7 | -18.6471 | -55.714 | 2025-07-09 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.9 |
| 76d69a81-7046-3ae7-874c-19d09c910d88 | -17.3367 | -47.5011 | 2025-07-09 00:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 3d3c9f5a-f976-3bc5-846c-41aa4917da10 | -10.5776 | -49.1316 | 2025-07-09 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 1d468f10-3cc7-3843-af0b-3334a23fbbae | -6.1792 | -48.0494 | 2025-07-09 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| e7480d7e-6554-30f5-9a95-e72a818fdb91 | -18.6467 | -55.7351 | 2025-07-09 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.6 |
| 44b203ad-1b31-3cb2-ace7-1d574a1fddde | -8.5025 | -43.285 | 2025-07-09 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 229.8 |
| e9e0b178-092d-30f1-ae57-f75fe31fb19a | -8.5028 | -43.2614 | 2025-07-09 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 19b809f4-b152-3cbb-83d4-34c0ff532696 | -8.5211 | -43.3063 | 2025-07-09 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 198.9 |
| 5dde7a9f-59ed-3df3-9357-6c7f2ddce32d | -10.5779 | -49.1098 | 2025-07-09 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| cd63fca1-57a8-3a48-9bfb-cb1a73c4d129 | -6.1794 | -48.0277 | 2025-07-09 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 1a856543-4b05-388b-a99a-5508a6a01485 | -6.1792 | -48.0494 | 2025-07-09 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 0a521e68-078c-341b-9250-6ca74acc252d | -11.6737 | -43.7762 | 2025-07-09 00:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 6d7bb2b1-b039-363e-9131-75fd0664f1b4 | -8.5025 | -43.285 | 2025-07-09 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 307.7 |
| 42cfcb91-2465-3d51-8d42-cde82a30a2d1 | -8.5214 | -43.2828 | 2025-07-09 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 379.8 |
| b993acc7-d664-384b-9ca4-11266e5f1f5b | -8.5211 | -43.3063 | 2025-07-09 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 788fd2e1-90a2-3dcd-a370-8ab096ab6fef | -17.3367 | -47.5011 | 2025-07-09 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 44.9 |
| badf9e06-1997-3607-94dd-2e3cf63ffe13 | -8.5028 | -43.2614 | 2025-07-09 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| e2ce0d53-dc56-322c-9268-ba1a847dd317 | -18.6467 | -55.7351 | 2025-07-09 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.7 |
| 5dc26caf-b2e0-3131-b31c-aec7c1e4e3d0 | -6.1794 | -48.0277 | 2025-07-09 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| e509b14d-27b6-3c46-851d-52d5a89e3a0b | -8.5022 | -43.3085 | 2025-07-09 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.3 |
| d95c0dca-796b-3483-9c96-e738ab83dc05 | -6.1608 | -48.0289 | 2025-07-09 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 48.6 |
| f23a0f33-cefa-3fc5-aae4-a7871f79ab5e | -5.2328 | -45.2102 | 2025-07-09 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 219ecb62-a657-387e-a386-5eebdef0b61e | -8.5217 | -43.2593 | 2025-07-09 00:30:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| bebca32c-1c1f-3f20-8f83-d43efdcd7313 | -6.1606 | -48.0507 | 2025-07-09 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 730e9a2c-6c2f-3724-a008-c0de380169d5 | -11.4526 | -45.106701 | 2025-07-09 00:35:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e11eb844-1785-3955-b1c7-f95856338874 | -9.4818 | -48.677601 | 2025-07-09 00:35:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef76c579-1d28-3de2-9699-ce653ee51ab2 | -15.7827 | -48.240898 | 2025-07-09 00:35:00 | METOP-B | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 72ac5154-b731-390e-b8b8-7348ebf0b88a | -11.4694 | -47.919102 | 2025-07-09 00:35:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a02b0571-e156-3a62-85d9-e540f9a1a8e7 | -8.5031 | -43.292 | 2025-07-09 00:35:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 71c310aa-f3b5-3ca7-9c20-35ff31a9350b | -10.6426 | -44.4692 | 2025-07-09 00:35:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d6f798c7-c2d4-3d5f-a8c9-4c5c117c90e7 | -11.4198 | -45.099201 | 2025-07-09 00:35:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b314fd85-b7e0-3fe7-8d6c-cf56c4627cf1 | -11.4623 | -45.104198 | 2025-07-09 00:35:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cac1279d-14c4-3f82-85bd-d96ddf185f20 | -6.1757 | -48.0369 | 2025-07-09 00:35:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ef0990e-19c1-3c18-93d2-efe32c2f4701 | -11.4354 | -45.079201 | 2025-07-09 00:35:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b156d828-d76a-3b0a-8570-e36c40936aa8 | -11.1038 | -48.858898 | 2025-07-09 00:35:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 450293cb-a451-3459-97ff-86a2943f751d | -9.233 | -48.585602 | 2025-07-09 00:35:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32d9e826-b1d3-3ef0-b3d7-ffcce7772646 | -8.5087 | -43.314098 | 2025-07-09 00:35:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d73a9bc4-1064-36f9-92c7-f5ff93491873 | -11.8801 | -58.6945 | 2025-07-09 00:35:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 79542470-1ba5-382e-b738-6d6073abe868 | -6.1562 | -48.0415 | 2025-07-09 00:35:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3122adfd-b130-3977-ba13-4fbe395b9d3d | -11.4236 | -45.114201 | 2025-07-09 00:35:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc93e3f6-a114-30f3-867b-7009ba58d263 | -9.221 | -48.5783 | 2025-07-09 00:35:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eca2b6d6-4c2f-37f6-ad4a-1eaa5ac4c829 | -9.4052 | -48.441502 | 2025-07-09 00:35:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 77aa54a6-7b14-3b1f-a18d-2e52828cf344 | -8.3104 | -55.0937 | 2025-07-09 00:35:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c350419d-7fa1-3c3c-9d01-ce9b95de54af | -10.5759 | -49.116001 | 2025-07-09 00:35:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 69fad167-de6c-398c-9a16-df00d7b6855d | -18.6474 | -55.7169 | 2025-07-09 00:35:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c1e2dbb3-023e-3461-998d-58c4ff8cc741 | -10.6343 | -49.453999 | 2025-07-09 00:35:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56796279-c510-32c0-a3fb-f544d9649aef | -10.1876 | -51.139198 | 2025-07-09 00:35:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b2a938c7-a7b1-3d4e-9c9c-d9adc2b019c4 | -5.5866 | -52.0756 | 2025-07-09 00:35:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84073453-2997-37c0-a8cb-4ad338e8b0b7 | -18.645399 | -55.706299 | 2025-07-09 00:35:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 569ffb3c-af31-3fd6-b6cb-2c1e6cfba478 | -11.4161 | -45.084301 | 2025-07-09 00:35:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2ca50b2f-cb7b-32f5-a813-2597ddb12342 | -11.5067 | -48.947399 | 2025-07-09 00:35:00 | METOP-B | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 16d97767-b3fc-3232-9bd4-ebce6c3f781a | -11.437 | -45.126598 | 2025-07-09 00:35:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a0718997-47f3-35cb-96e5-ddaa2e8f79bc | -13.3926 | -47.8825 | 2025-07-09 00:35:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e858c1cf-58c1-3320-9ac5-ae18604a7475 | -8.312 | -55.101101 | 2025-07-09 00:35:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e2abb72-322c-3906-b453-b771f1d4aab1 | -8.4975 | -43.269798 | 2025-07-09 00:35:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6a1f482c-b11b-33fa-a146-892f5371a2ed | -11.4258 | -45.081699 | 2025-07-09 00:35:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 65731c1d-91dc-34f3-8f70-2ae5ec380858 | -11.4064 | -45.0868 | 2025-07-09 00:35:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 25894ad2-4379-3b05-94fe-4ce9b764dcb5 | -11.4333 | -45.111698 | 2025-07-09 00:35:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 357ba330-5747-3984-9348-08c3042993dd | -18.655199 | -55.7043 | 2025-07-09 00:35:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8e80478e-815b-32e6-8a95-8a2547806a8e | -4.5528 | -48.005299 | 2025-07-09 00:35:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96c1e279-cf7e-3139-97af-101cf7459ae5 | -11.6616 | -43.771 | 2025-07-09 00:35:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a1157d7b-64ce-3b07-a185-c09ef877a36c | -6.1687 | -48.050701 | 2025-07-09 00:35:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 95c5f989-b7e8-36ef-8ca6-fbbd13946a7e | -10.5583 | -49.129398 | 2025-07-09 00:35:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa883c55-ed69-37a6-b91e-6c9632edcd9d | -18.6572 | -55.714802 | 2025-07-09 00:35:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 49970037-37e5-32f1-9099-bde545451c9b | -11.4586 | -45.089199 | 2025-07-09 00:35:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 00367c5c-937a-32e8-8928-fe550684ef48 | -11.6712 | -43.768398 | 2025-07-09 00:35:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3731dcbe-6d24-39ce-8ffe-380f6290ad56 | -11.1059 | -48.867802 | 2025-07-09 00:35:00 | METOP-B | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c019f32c-8e50-38c0-9ec5-136c33f7aff6 | -21.431801 | -48.6343 | 2025-07-09 00:35:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 93b02700-bc5d-353e-a9b8-50735520bc3b | -17.3353 | -47.504398 | 2025-07-09 00:35:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 557c7c9b-f812-3fe2-8677-aae27609fd63 | -21.040001 | -45.2616 | 2025-07-09 00:35:00 | METOP-B | CANA VERDE | MINAS GERAIS | Brasil | 3111903 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5e20b5ab-0f72-3c31-87f7-5ecc25b003aa | -9.4796 | -48.668201 | 2025-07-09 00:35:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f10fc9c1-f541-349d-9b37-89c372d1e8d4 | -13.6311 | -44.405201 | 2025-07-09 00:35:00 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 914a7704-0507-3ab8-b90d-49f583e9554a | -6.1632 | -48.027699 | 2025-07-09 00:35:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2474ea04-fbee-3709-8b98-91d7f448e8bc | -13.3948 | -47.891899 | 2025-07-09 00:35:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6220fb66-9d31-3770-8fd7-67eb21eef392 | -8.5015 | -43.245098 | 2025-07-09 00:35:00 | METOP-B | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ac133d17-faad-3c0e-95d8-6509d4815671 | -6.1659 | -48.0392 | 2025-07-09 00:35:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ebdf6012-1030-39cd-97a6-16d8acfb9c38 | -9.4029 | -48.431702 | 2025-07-09 00:35:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8eb7ea82-168b-3065-9b5f-14d6db393890 | -10.5738 | -49.107201 | 2025-07-09 00:35:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1fd884dd-2909-329a-a0b1-52c73c5055ce | -10.5779 | -49.124699 | 2025-07-09 00:35:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7726310a-56ce-30db-b770-f1a2c72e494c | -9.4075 | -48.451302 | 2025-07-09 00:35:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 33ff4173-5ea8-33fd-a3ae-695d8ec812ce | -11.5087 | -48.9561 | 2025-07-09 00:35:00 | METOP-B | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ea589e9-0e58-3a56-9d87-c28a0dd8867a | -7.0878 | -49.154701 | 2025-07-09 00:35:00 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| b283f966-48fd-3bdf-b898-8a7409702ada | -5.2351 | -45.219601 | 2025-07-09 00:35:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2dc91f5-aee4-31ec-ac15-8f23bd32ec9c | -8.5127 | -43.2896 | 2025-07-09 00:35:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f9f4fb62-f5e7-35fe-a54a-f3e76f1aa163 | -20.391701 | -48.599998 | 2025-07-09 00:35:00 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 012e4a89-2945-337b-90dc-30a1b4cf2303 | -11.4101 | -45.1017 | 2025-07-09 00:35:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 938a17d5-db7c-3b7b-98e6-2c467a99073e | -11.4295 | -45.096699 | 2025-07-09 00:35:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cc95f8ee-6a77-33c5-8a0b-0efaacc07ad0 | -18.6434 | -55.695702 | 2025-07-09 00:35:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c0c2be0b-7be8-38b6-ae50-ddd2fadab03f | -21.433599 | -48.641998 | 2025-07-09 00:35:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
