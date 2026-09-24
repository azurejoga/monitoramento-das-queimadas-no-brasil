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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f25912e0-93dd-3c07-b4ae-76c111292be2 | -7.435 | -49.8354 | 2026-09-24 00:38:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f66de458-8ecc-34ba-956c-d3e8707e9700 | -4.9917 | -45.5438 | 2026-09-24 00:38:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c51fe94-18d4-3202-abc1-2f7cbb14883e | -4.2973 | -49.134102 | 2026-09-24 00:38:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c97a6193-9358-3a99-bd9b-f427e6950f92 | -10.0959 | -46.001999 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62ca1642-fd4e-36ef-b55e-495b848b7064 | -12.6875 | -46.997002 | 2026-09-24 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 90e67cc0-a05e-34b3-8a6e-2f34aad0c631 | -15.5663 | -42.353298 | 2026-09-24 00:38:00 | METOP-C | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f755841c-76ee-3341-956a-1e85fcbb961d | -9.8536 | -48.502499 | 2026-09-24 00:38:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67f65f2d-e901-39ac-b3b1-0c8b7a643b0d | -12.1345 | -45.621399 | 2026-09-24 00:38:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fdf683fc-1ad1-3a5e-9aa5-d322acf36833 | -1.4219 | -54.586498 | 2026-09-24 00:38:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95b92433-3465-37cc-b770-d315e80cf4b2 | -3.2306 | -54.322498 | 2026-09-24 00:38:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6607364-1396-312e-a9ad-8c8343c5b2a2 | -5.5807 | -42.730099 | 2026-09-24 00:38:00 | METOP-C | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9e66c387-d004-3c08-ab45-ceda419b525c | -8.8174 | -50.452301 | 2026-09-24 00:38:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7909b42-9a04-33db-a15d-192f54d83635 | -9.1502 | -49.959599 | 2026-09-24 00:38:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffe9e7fc-95d9-3442-bae7-eccab4019fdf | -17.4259 | -42.461498 | 2026-09-24 00:38:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 80a9ab04-dd51-39e2-8c32-861d35bb228a | 1.2922 | -50.843601 | 2026-09-24 00:38:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 855c4127-c882-31cb-810d-7c02324c2a93 | -3.4134 | -53.994999 | 2026-09-24 00:38:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dea9c111-780d-3444-b85b-fd030124744a | -9.8521 | -48.495499 | 2026-09-24 00:38:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a6a6a06-9c45-3ac6-b099-1f3dc9bc07e9 | -5.0015 | -45.5415 | 2026-09-24 00:38:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ddbb2ae9-34e5-3e49-a37b-8a731b2704a3 | -4.6684 | -45.969299 | 2026-09-24 00:38:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cea68459-2763-3af5-b9fe-95fd40bcedcd | -8.7556 | -45.834301 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fdeacc3c-10c9-38b3-bf45-aebffc9d3b9e | 3.8371 | -51.800201 | 2026-09-24 00:38:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c41c0258-a5bb-3e60-9177-a31466135485 | -4.3055 | -49.125099 | 2026-09-24 00:38:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5104853a-4467-3c53-b9b7-da26d61bfea4 | -10.8794 | -45.0695 | 2026-09-24 00:38:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 17057524-b395-3361-a7c3-4fe338d30737 | -10.2711 | -49.960899 | 2026-09-24 00:38:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4d570add-9a02-3c1d-b939-2dbb70c36a62 | -10.7186 | -48.732101 | 2026-09-24 00:38:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca25bd59-5c64-36af-81ac-f7288d4ae125 | -12.1951 | -47.008202 | 2026-09-24 00:38:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b55f0483-a7ca-3c4c-bfef-10097c0e4cf1 | -8.4543 | -48.692902 | 2026-09-24 00:38:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 830e3255-e21c-3323-a50b-82a76cabc84d | -1.334 | -47.778999 | 2026-09-24 00:38:00 | METOP-C | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 054702f8-f62a-3d8a-8a7a-a2880b787500 | -5.5801 | -42.3013 | 2026-09-24 00:38:00 | METOP-C | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ca945fac-1e05-300a-82b8-fe8a0700a85b | -5.6686 | -42.5821 | 2026-09-24 00:38:00 | METOP-C | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7d44bfce-4e54-344a-ac68-8e33037dc0ad | -12.5083 | -46.979698 | 2026-09-24 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d28ab31c-30b4-3c38-953a-badecaf5a5bc | -15.2382 | -43.265701 | 2026-09-24 00:38:00 | METOP-C | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 6527d470-9bef-34d9-bf1e-a486488ddd2e | -10.8465 | -43.243599 | 2026-09-24 00:38:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 00394c8d-166b-32aa-afa0-9cd24501c9b4 | -6.6505 | -43.619701 | 2026-09-24 00:38:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c117047a-6f88-33f2-ae1b-b94b5d219693 | -3.1733 | -48.0154 | 2026-09-24 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d2148da-f64b-3149-a793-e061cc3046ab | -5.7521 | -49.9533 | 2026-09-24 00:38:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc8d5fdb-d16e-31f8-b8dc-354e22c95643 | -11.5212 | -49.197201 | 2026-09-24 00:38:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f0961e7-c29b-3ef5-87cb-d7e9b19d52aa | -15.961 | -42.9571 | 2026-09-24 00:38:00 | METOP-C | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7f2f1a29-822c-3105-bd5e-e06cea6169a5 | -12.8558 | -44.379902 | 2026-09-24 00:38:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3f7f6ce8-1cbc-3c99-8ba5-439e0e71720a | -8.8994 | -46.8069 | 2026-09-24 00:38:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9e3948a-0ec7-3fa2-aecb-42e47fb21ed1 | -8.9197 | -43.868 | 2026-09-24 00:38:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1e19aaf8-aa87-3fbc-b92d-c1ce28c22fa5 | -7.03 | -44.6474 | 2026-09-24 00:38:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a939a64-6b88-3659-bf33-18f202edbe65 | -6.4234 | -43.490101 | 2026-09-24 00:38:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4492459-3766-3fa5-b65c-8c721fcd6a90 | -6.2205 | -47.494301 | 2026-09-24 00:38:00 | METOP-C | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36717bf5-e12e-31ad-a4d4-71b8933d94ed | -12.5067 | -46.972801 | 2026-09-24 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3789f8ce-1771-3225-850f-273a811d9106 | -8.2514 | -48.208199 | 2026-09-24 00:38:00 | METOP-C | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a40aa570-0381-3de7-bad5-2d9ad86a7f63 | -8.253 | -48.215099 | 2026-09-24 00:38:00 | METOP-C | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 879698bc-4c16-3e74-9c17-5f5557551ad2 | -4.0252 | -52.058899 | 2026-09-24 00:38:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba623c2c-29ae-3493-a94a-439921bce644 | -12.1013 | -50.7341 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a108bffe-41fe-3354-819a-9d6b3e459c3d | -11.2717 | -51.357601 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9e6c4bc4-7c3a-33bd-8d6f-091f4b0db5ba | -11.7928 | -50.968399 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c24a8891-d158-315e-9588-7ed4e82ec7f7 | -3.4157 | -54.005299 | 2026-09-24 00:38:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b71f2d4e-257c-3282-b5ef-9bb3a0af3d24 | -8.2931 | -49.898499 | 2026-09-24 00:38:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94f82b03-4ee3-3747-8144-580804705ab2 | -5.2029 | -44.689098 | 2026-09-24 00:38:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac234e97-5c85-370f-9643-87d45ad261ad | -6.4307 | -43.477402 | 2026-09-24 00:38:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cceae3b9-f89b-3cd4-9158-d56c08ac817e | -11.9563 | -50.7747 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6ac493e2-f0bf-3293-95cc-bcba5ab225f2 | -10.2155 | -44.144299 | 2026-09-24 00:38:00 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4853c6be-baed-3b9c-aeba-ff537a2961e8 | -8.7787 | -45.8447 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 08bea898-5874-3276-804d-ebd74244e38e | -11.4902 | -42.320999 | 2026-09-24 00:38:00 | METOP-C | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3d14633b-4da7-318d-ba90-03a36da24d3c | -11.7909 | -50.959499 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9f2ee79c-fd4b-3069-9360-50f7e4241842 | -6.424 | -59.9576 | 2026-09-24 00:38:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0002c2d-48fc-3d95-987c-0b9049e19d0d | -5.8315 | -53.849201 | 2026-09-24 00:38:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f363541b-e72d-3543-9af4-35ae7960c964 | -10.2677 | -49.9454 | 2026-09-24 00:38:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d130649-513c-39c9-8459-3cdb46f41f6e | -3.1576 | -50.822899 | 2026-09-24 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04dd941c-8639-382c-81ad-d0a3a8c98bd6 | -13.7922 | -54.050999 | 2026-09-24 00:38:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 54879c5f-6c64-3db9-adde-1798b806c5d4 | -7.134 | -48.417301 | 2026-09-24 00:38:00 | METOP-C | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0b5bea9-2642-3462-a396-e4603a28c999 | -10.7583 | -44.819099 | 2026-09-24 00:38:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 47f43855-ea7f-3632-b2c2-35ad964717b8 | -8.1526 | -49.546902 | 2026-09-24 00:38:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca981523-4e4d-3700-ac3f-fe0f15eb7147 | -8.151 | -49.5397 | 2026-09-24 00:38:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 771981b4-332f-3f06-a1b8-e77dcefded5c | -10.1074 | -46.007 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2679e155-a9f2-3f56-9828-0063f25844ed | -10.8812 | -45.077202 | 2026-09-24 00:38:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 312bc167-7bc5-39fc-9818-a0e80bf25d98 | -10.7202 | -48.7393 | 2026-09-24 00:38:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b1c693d-1818-3c0f-8093-146486bd1a15 | -10.9671 | -54.089901 | 2026-09-24 00:38:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ceb922e9-1d73-3cba-88f5-70df17241761 | -19.187401 | -47.362499 | 2026-09-24 00:38:00 | METOP-C | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b361909f-b108-3467-8efc-96b39438d3f7 | -4.3071 | -49.131901 | 2026-09-24 00:38:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a5b88d2-c528-395b-bb0f-b4e413de0636 | -8.1972 | -54.721802 | 2026-09-24 00:38:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 617f442b-0807-3ec4-a44d-0330cf4ad20f | -9.5735 | -40.309898 | 2026-09-24 00:38:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a4d75ede-f4d4-3ce9-88e2-e16b2b360f27 | -5.7537 | -49.9604 | 2026-09-24 00:38:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2dff5c05-60c0-361e-a24b-314f7f1b61e3 | -4.9112 | -45.640598 | 2026-09-24 00:38:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64035e20-4b9c-3d8c-9be1-5e8db93ef380 | 1.2824 | -50.8414 | 2026-09-24 00:38:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 08f4e3c6-4514-33cb-8407-627e01df4a00 | 0.6088 | -51.5718 | 2026-09-24 00:38:00 | METOP-C | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7dbc2252-346f-3e9c-b3a3-ce023fcb1117 | -9.2672 | -46.2565 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9eb45628-86a5-372c-ad6b-d01fba4c053e | -3.2048 | -49.0924 | 2026-09-24 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d416b5a-0507-3020-8765-85751301d314 | -4.027 | -52.067101 | 2026-09-24 00:38:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99f3b697-b3e4-3ae4-a6d8-e326e83d8d76 | -9.2397 | -47.388901 | 2026-09-24 00:38:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c82643d3-65a4-3b44-bd10-87ba6185ce6d | -10.1429 | -45.540298 | 2026-09-24 00:38:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3e04777b-e08d-39d4-a7e1-7fcacbbb9b77 | -11.2385 | -51.394001 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9692dce3-fc62-3caf-8f76-b2ab9cc9452a | -15.2459 | -43.254902 | 2026-09-24 00:38:00 | METOP-C | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 784034d6-6351-3b2f-8d2a-59673c1cffd9 | -0.9312 | -47.5532 | 2026-09-24 00:38:00 | METOP-C | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 914f7b13-fd41-3122-b56b-40f221570390 | -3.5267 | -49.3713 | 2026-09-24 00:38:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c687a40e-2335-38c8-b069-6fd3ad7177f0 | -10.9768 | -54.087898 | 2026-09-24 00:38:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9616cef7-26e7-38d1-bc04-c3e999a6ab6e | -11.3655 | -43.380001 | 2026-09-24 00:38:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cb833831-8d02-31a4-b39d-a4ca8194d9e8 | -7.1934 | -47.463001 | 2026-09-24 00:38:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 091ec857-f7f1-30fa-ac02-4f6740adf725 | -6.4214 | -59.8969 | 2026-09-24 00:38:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6086b34d-a54f-3ef2-9d3e-63dc147e3b79 | -3.5594 | -43.452 | 2026-09-24 00:38:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5fbd88f2-18f1-3b9f-901b-a77c4ac7dae4 | -6.1281 | -44.587799 | 2026-09-24 00:38:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8237275e-0705-3e66-92b7-e931d1dcb22d | -7.4334 | -49.828098 | 2026-09-24 00:38:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b68da1b5-0e07-3b10-9a4e-c621c991cc58 | -14.0102 | -42.894402 | 2026-09-24 00:38:00 | METOP-C | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ad131178-f7fc-3d8b-83a9-2a86386e21aa | -8.2416 | -48.2104 | 2026-09-24 00:38:00 | METOP-C | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b66ac85-076e-3f61-bffb-2e1cb015a873 | -10.1091 | -46.014301 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README16.md)
