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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9487b5a1-d6e9-366b-9aea-80e0bdf29f31 | -11.04165 | -54.15553 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5290efe5-e09b-35b9-8bc2-18396a137bd3 | -11.49806 | -47.74477 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc0a6202-0528-3c94-80f1-8413cf83dfae | -9.02242 | -48.75274 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0dd61856-7e1e-3004-ba7f-3381f060f92a | -8.07823 | -45.50561 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53d46d22-2ee6-3087-8c12-0f404f547fe7 | -11.86555 | -48.98526 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bbaede3-fb91-3979-9c88-4b7666516f9f | -13.8855 | -48.58826 | 2026-09-20 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ce6f3be-5cbc-3e62-8184-757365a4171d | -10.28244 | -50.24317 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7160c143-abf4-3f92-a1ff-96aaf415f22f | -7.85984 | -44.8534 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9b2df1eb-ccf3-3cc8-bade-9556c0ae0ef4 | -13.39773 | -49.455 | 2026-09-20 04:40:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ce978e3-4cad-3cd6-9871-ff2b55843a09 | -5.84452 | -53.55359 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bc1dee8-9f22-346d-a380-67410d54cfec | -12.88862 | -52.08596 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 174f1e45-6833-3bc2-b74b-d237e339e296 | -6.79043 | -47.80996 | 2026-09-20 04:40:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97e30519-3976-3143-b394-01471bec11ab | -10.66426 | -47.42941 | 2026-09-20 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69173e1f-43a4-39a1-86dc-55f3b96d145f | -9.22231 | -46.20778 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f94f0f4a-431b-368c-9467-7dec179ad4fd | -8.1701 | -54.74223 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0367b88b-3ff0-365e-b030-674969aae0d6 | -13.00924 | -46.92455 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dc590ba-909f-3cb9-9989-695e873b7188 | -6.72688 | -55.0732 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c1991f6-ef10-33e4-bb2d-cf2784f9bbd4 | -7.11993 | -44.82789 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44e2c578-70ec-32dd-8001-e0c9e6aeb2f1 | -8.77238 | -45.86044 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c6e8a13-4d18-343e-a75d-e544ee1106f5 | -8.36193 | -42.24134 | 2026-09-20 04:40:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6da26b5d-5451-3402-94ec-ca0fa62cdb47 | -11.24311 | -54.10429 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c83ff11e-dc30-33f4-a56a-35b3ca05ef0e | -11.7109 | -54.5628 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da3bf4fa-5e0f-3521-9070-cc782b16e20e | -9.26166 | -48.20535 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4540cf52-e51c-3c1a-b7c6-854239eea20a | -7.86051 | -44.84896 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f651fbe-a941-3b83-b996-389dd35aff9c | -9.71372 | -45.86892 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 801c8d6d-9cea-33b1-b2b2-ee15a8b64e51 | -11.47269 | -45.33648 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fd59040-744e-3140-8279-17852111ccb7 | -10.09862 | -48.43225 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd0c66f9-1aae-33c5-8c04-2a3a3129aa45 | -13.03045 | -46.92717 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60e8354e-4b6d-36b0-98c4-5456b916f2e3 | -8.43332 | -46.86068 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f58dfb7-eca4-3529-a9ab-4b362f7dcec7 | -9.7978 | -45.06655 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d990301e-b9fd-3557-882d-36c1e0a27313 | -7.01976 | -45.2403 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb560228-3908-3622-a3a6-fb22c1e90c4e | -8.24788 | -45.60014 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f91298af-c1cc-3e92-b7a7-cce793733f1d | -12.7693 | -52.85991 | 2026-09-20 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 004e8539-38c7-35c8-980b-1f2be3a665b0 | -10.87216 | -56.23076 | 2026-09-20 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c01ef2f7-4d3c-3143-9f08-9789915aaf7e | -7.30313 | -46.74415 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d37c1543-6735-361d-88f4-0382b708cd5f | -9.35068 | -50.11284 | 2026-09-20 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d305449-73ca-38d3-8900-b0f128b8e9cd | -11.34587 | -44.18909 | 2026-09-20 04:40:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40cc9c89-ab61-3807-bda1-8356181e1654 | -11.48063 | -51.47968 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c837b769-1658-3ce1-a5c1-dd7480161eb9 | -7.18429 | -47.89704 | 2026-09-20 04:40:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9c3fb1d-27a8-31d9-8d98-5e4cb9bba18f | -10.3814 | -48.31848 | 2026-09-20 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9257a49-b5a2-3bc7-a028-64562ae38d24 | -9.21528 | -46.23071 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d3b9e62-bca0-38fc-adce-3ff62e3828f3 | -11.7728 | -47.45743 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa116fc9-8d5e-35ed-8b43-8fe2c2eb9c3b | -11.95251 | -50.1026 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ad6a0c4-abb2-3804-bfca-b425aa77aa99 | -10.28124 | -50.55686 | 2026-09-20 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 469567ff-9052-345a-9a7b-88c0406fc9f9 | -12.15896 | -47.03054 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5fce77c-c9ce-33e8-ac0e-369e592b55f2 | -6.10277 | -57.68729 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1adc6cef-27bd-3b75-9c84-30239e48b8f2 | -9.81042 | -48.32122 | 2026-09-20 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5048a3bd-4bbc-35d5-a6ae-9de54364e106 | -11.37331 | -51.40677 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c0208139-2d62-3ec1-a58a-9c05eedfeec7 | -10.91111 | -53.97374 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1bf856be-3329-36b4-b856-8af502bbbeb2 | -6.34369 | -58.30226 | 2026-09-20 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9e1ce84-9315-3f67-b27f-c84c6707cf63 | -13.73337 | -48.78282 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8ab0931-5cb5-38c1-9829-573dda3eeda2 | -9.78791 | -45.05584 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6b0b1a6-01ac-365a-a70d-51ac9e339ea1 | -8.5019 | -47.43977 | 2026-09-20 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a49eee0e-1e9c-39f9-bddb-0a90931b1731 | -13.62004 | -46.92093 | 2026-09-20 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91100010-25c0-3dfc-a222-8f225acb3c77 | -13.24436 | -51.74065 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8bcbffc-13e9-3e41-9cd2-b78168383d4e | -8.04746 | -46.25291 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 9bc4284d-9416-3d9d-b083-41c0614f07be | -5.86532 | -52.03387 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8a0de8c-bc7d-3ce5-948c-c23d0c907054 | -10.261 | -49.99262 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e6255d9-9977-34f3-b35b-bace250a453c | -10.40457 | -48.92595 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f68817c-10bb-3fa9-b9d1-fda47b609d34 | -10.27221 | -50.26375 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| f33c229d-ca0f-30ea-bde6-0e9abd6997a6 | -11.38114 | -51.42394 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| beeb7eca-5dae-3773-aa26-3940d41158bd | -11.86065 | -46.8757 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1ba098c-6367-36d2-ac8c-29aa649cae22 | -11.86941 | -49.00394 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dbcd8451-2f8c-3a0b-93b6-9f2b07ee8a9d | -11.4537 | -45.36159 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 532b3784-0aea-33a6-b83e-cbc1731c567d | -9.17497 | -59.42416 | 2026-09-20 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7f4f9d9-8582-3aeb-8929-fb4ea2f18d67 | -13.02099 | -46.91803 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25d3d770-ad16-3822-93f4-ef509904ab67 | -7.40823 | -49.84022 | 2026-09-20 04:40:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ced58a57-b159-37bb-a46b-76d8cb11fd8b | -9.7731 | -46.07653 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebe1f274-3376-3095-8fce-0ea7b5cde12f | -11.00016 | -48.31179 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a24a1e3d-ac34-3f9e-9dfa-5967f9c41813 | -11.23991 | -48.38625 | 2026-09-20 04:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e4111e29-53c3-305c-9276-8435af491171 | -8.17663 | -54.75641 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 884b436d-a3cb-3115-86e2-23466ccc1b2a | -10.30497 | -45.25878 | 2026-09-20 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5201c2a0-83d6-3ae9-848f-3dad3ff2ea75 | -6.33517 | -55.29644 | 2026-09-20 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5a77c57-5c6c-3ac1-89fa-61010c050c32 | -11.12168 | -47.72837 | 2026-09-20 04:40:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d26f5a9-d598-3b4a-849d-0422fc97ae14 | -9.6825 | -54.3334 | 2026-09-20 04:40:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccaac464-dbe7-3e31-bb41-a90864c17f00 | -7.56843 | -46.36275 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06df9537-3ab8-3e75-b368-4986366dba63 | -11.03671 | -48.31376 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ff798f1-b9ed-3cb7-91f8-8830ca42974d | -7.59549 | -55.71363 | 2026-09-20 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2d25c29f-cda0-34b9-9515-9b1261ec4d62 | -11.07727 | -49.50151 | 2026-09-20 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bf3c38af-b0c0-3513-b49e-c03398b271c9 | -6.81814 | -47.89241 | 2026-09-20 04:40:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| def0d926-bdb5-3bc6-9bfa-8ab1d3d940a9 | -9.78856 | -45.05131 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0966e526-1035-3264-ae7c-c55dbab64504 | -8.49966 | -47.43213 | 2026-09-20 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23aedac5-1176-331c-9595-4ca53a75f094 | -11.3755 | -51.41506 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 70ba4fdc-a23b-3b63-b612-386896f6e78a | -9.35009 | -50.11646 | 2026-09-20 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11b37e3a-e0be-3602-8286-cf7379636a95 | -9.12311 | -45.71554 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b2b5740-0c64-320f-bb82-a0fac492304c | -10.68966 | -60.7344 | 2026-09-20 04:40:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19f9a45c-cb5e-3361-97e9-472e9a2eaf4d | -11.88321 | -49.00257 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 420b846f-daa7-3f40-bfff-c1fe1da1cd72 | -11.76598 | -47.43329 | 2026-09-20 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e50db017-1c61-3275-94de-cfbf494bc634 | -13.39441 | -49.45445 | 2026-09-20 04:40:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cdd60c2-869c-3ca4-a065-61aff377d2c3 | -7.5359 | -45.88675 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c548ed5-b1d9-3f24-8779-f1ff0bbc8d78 | -12.12304 | -47.03292 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 600b3f46-4cae-3c62-9f1b-823e2f46e3bd | -6.7261 | -55.0778 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d6302189-8b5e-32fd-b04d-0da162175cfc | -13.19377 | -51.75203 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5135ef0-4d3c-3c47-a53f-adcbd652a144 | -10.31572 | -50.21877 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 203c1079-bfb8-3499-93b6-76fc8fe12fe1 | -9.12064 | -45.73186 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6e31dff9-6dc6-3e59-b270-7c384f9f35b7 | -8.2371 | -61.37971 | 2026-09-20 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5bea9ef-15c6-3115-8f28-601cc1594000 | -11.77566 | -47.43866 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c99806d-d758-34a8-88c5-3625dc974cce | -11.44581 | -45.33703 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a894b990-294c-3dfb-ba74-fcd2b1be760a | -11.48345 | -51.48413 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e13fc0bf-8b9b-3968-a84d-a4668e83f468 | -13.87792 | -50.27967 | 2026-09-20 04:40:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README65.md)
