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
| 6f5e8776-406b-385f-867c-95c046a107ae | -4.05409 | -56.33238 | 2026-09-12 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 876dbcf8-69f8-3c1b-88ed-11c9abf998ad | -11.08258 | -50.83747 | 2026-09-12 05:10:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 814a4da6-cc1e-3f38-9b0d-ac456b555bea | -6.80195 | -58.79153 | 2026-09-12 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24258024-7c47-3af8-91bd-81ac5087d1fe | -10.55299 | -51.34678 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55dd0f87-adea-3fa9-b391-4d139e462b91 | -4.52284 | -54.95309 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58a8a215-f579-3f69-9022-882929721927 | -6.28267 | -59.93022 | 2026-09-12 05:10:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39bddce3-fdb5-34dd-92b5-b994368f9e59 | -4.70364 | -55.99754 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6255ce5-3ea6-3e95-8589-97e0fe85c89f | -6.31819 | -56.05859 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7463d0c-6187-3399-8dc4-429f06515269 | -10.34556 | -48.09167 | 2026-09-12 05:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55a878df-e141-31e7-b4d1-e8af1ff6bf2e | -6.39891 | -55.20446 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7043c1b-7ca9-38de-aa2d-f8c8df12138b | -6.10964 | -55.63817 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0183739-c7e1-366b-bd48-6d72dfcdbf92 | -5.76754 | -45.08891 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9e7db33d-1669-39d3-87c9-40d31ac6acce | -4.53571 | -54.95884 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d10e263c-533c-3602-9201-cda615fc58b9 | -5.79991 | -53.81968 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0de24c6e-bc5d-3abc-a9d5-9242be0742fc | -3.79212 | -52.13137 | 2026-09-12 05:10:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07a8b775-1db2-3239-a323-8966ce7eef58 | -7.41797 | -46.15952 | 2026-09-12 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fdd8ee65-11d6-30b4-8852-581469d88e44 | -6.24474 | -51.70265 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 41b83405-ee01-3c6a-aabd-62ddb6b98c46 | -8.5771 | -54.56674 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd9acb72-0999-3493-9496-c919d39a32ce | -10.5192 | -51.34138 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5378ab5-bed0-3093-bab4-f8f38db4d8d1 | -6.23067 | -51.70053 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3f08b5df-7ff2-355a-b438-60be64bb6d34 | -6.24243 | -51.69428 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79c595e2-f26e-38e9-8acd-36fa74b7d443 | -6.18804 | -57.72469 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a583703c-1348-3e8b-b237-b00f53db6fb3 | -10.62667 | -46.12616 | 2026-09-12 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f3dfcbb-529b-3407-8979-e8b8324da3d5 | -10.50426 | -51.31205 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef6d608c-153b-3b50-a4b7-222df7e37d87 | -10.89555 | -47.83685 | 2026-09-12 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 92491b0c-a976-3139-b8a6-33c2cba2c104 | -10.52851 | -46.34319 | 2026-09-12 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb030bca-8493-3934-804f-23be39fa592e | -5.8248 | -53.79159 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da27a7a6-5c09-30e0-aaae-06f434417d02 | -10.53177 | -54.38002 | 2026-09-12 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc533f7b-9c35-30bd-9dc2-5d2f36b6fda9 | -5.48853 | -45.13046 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cff3413b-9205-37fb-801c-49744a97f572 | -6.956 | -44.54033 | 2026-09-12 05:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec5bcb85-1eb0-357a-97dd-b028b3a4ec8f | -4.92898 | -55.79013 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1420f99-caaa-316f-a8dc-d195a0ec87f2 | -6.24595 | -51.69481 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92771513-dd4a-38e1-b93e-4eabac169035 | -6.51906 | -47.61056 | 2026-09-12 05:10:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e3d23b0-9f46-3623-bdc8-2c632c187256 | -6.28594 | -56.01908 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ea48aa5-352b-35ad-8b25-779ed825ba17 | -7.17488 | -45.88743 | 2026-09-12 05:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2e6aafb-507d-36cf-8605-c3e6efaa0f90 | -10.5579 | -45.20777 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26b58e5f-53bc-32b9-82dc-2062a640b7c6 | -6.19614 | -57.72155 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19cb5ab6-17f8-38eb-84ad-9b8ae20b24cc | -7.84695 | -56.58091 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69c62e5a-cd39-3d63-8ce8-52d017af1d81 | -8.07227 | -54.85435 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a914b65-39cf-35ea-9eae-d18692e31909 | -6.60773 | -58.85065 | 2026-09-12 05:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2252c4c5-b483-3685-a71b-f1b817f70121 | -10.55741 | -45.2115 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f9d647b-5f7f-3dae-9104-f171540b5928 | -6.84511 | -55.80357 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86aae288-9587-3ccf-90ed-2a1f48d33503 | -6.88167 | -55.64294 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd3fb761-ea6f-352c-ad29-24a481d1ba9e | -5.82261 | -53.80547 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c76a1e56-d375-3d07-ac51-308f0c880947 | -4.51948 | -54.95255 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8eac1a78-e4cb-37f0-99c2-ee622681266d | -10.55817 | -51.36339 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1a51b20-6774-3d98-8235-4e25d1fef4ee | -4.53861 | -54.91925 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92c708c3-f9a4-344f-8256-ff08d1f72302 | -4.65705 | -55.7477 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af4ab381-daa1-35b7-8ff6-9b52b70115f2 | -6.10731 | -55.65276 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90606542-f03e-343f-afca-5c293ae481f2 | -10.50496 | -51.30721 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1c884df7-5031-3569-85ec-b72ef3759514 | -6.28473 | -56.0265 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d605bab2-1d66-36c0-b99d-43763d9fb6d0 | -10.56294 | -51.35739 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1040c0c8-0828-3500-82ef-99e9cb5d97ef | -3.73413 | -61.75463 | 2026-09-12 05:10:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 77b9a2c3-4da9-3fdf-af84-0ed4a8c3b737 | -9.71418 | -54.34832 | 2026-09-12 05:10:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 635ad8f1-4d03-3ef4-8676-d5b717786f4e | -4.86951 | -56.00335 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a5e753e-be55-3c3b-96ec-afe2043eb518 | -6.11481 | -55.65358 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77f6e2f6-d554-39df-a473-05aa19543d94 | -6.40475 | -54.97439 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ee84296-90c6-3993-b362-4093002fbd7f | -4.87011 | -55.99964 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57f008d4-5ab8-3ee9-953c-b2f589ed7344 | -6.07099 | -53.49514 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8a39154-bdfb-32c9-a143-8fafa44328e0 | -5.76085 | -45.09755 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b0c977f8-b63c-39b4-8826-c053409a08cf | -6.4286 | -56.1096 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0caf2ea6-9a99-370e-bc45-7c8daa405c94 | -4.87297 | -56.00392 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76539658-9704-3fb0-a8e2-01d579586210 | -9.72898 | -53.9581 | 2026-09-12 05:10:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e58f5e5-755b-3cda-b989-d832bc08efdc | -7.19088 | -45.92334 | 2026-09-12 05:10:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42f3742f-cba7-38de-924b-a278982f7bf2 | -6.18151 | -57.74144 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| da920104-b11c-359e-b694-f5534c78537b | -5.76602 | -45.08834 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 50546319-a76e-3bd3-b304-c0c205bcd6bc | -5.86555 | -52.10622 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62e4036c-8a0d-39a3-bf57-65009d7aabe2 | -8.08169 | -54.83798 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5805174f-62e0-3f18-8b9a-2ccf2a962f06 | -7.60652 | -43.96341 | 2026-09-12 05:10:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f67c695-901d-3bd5-87fa-afb772690fda | -2.67156 | -57.5063 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 430dbbd6-4616-3ba8-b6cb-68c896cf6d4a | -5.79968 | -57.71934 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11ed7c09-5568-3fdf-8aac-a9ad3375247e | -11.41609 | -43.94788 | 2026-09-12 05:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba9f1a4e-5046-33d2-878e-9ae375d7c5f7 | -8.11502 | -54.79312 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edecc3c1-6b52-3182-9b7e-994bba8db8b9 | -4.54026 | -54.93041 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb6c57dc-bcd3-35fe-9216-2e41da4812c1 | -11.40429 | -43.94147 | 2026-09-12 05:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c589c3c0-c38c-31cd-aa02-2d487c65eece | -4.91792 | -55.81487 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab3a3cfc-1167-3792-ba89-01418721ad4c | -8.53662 | -54.69992 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7d1c46e-6ed5-3349-88a6-7bba2107d302 | -8.1189 | -54.79017 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7795dffc-44e2-3248-a968-f306e45156c9 | -5.86498 | -52.1099 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d56f2a4e-a066-3793-91ab-82bc73e5a084 | -10.55366 | -51.34224 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e0160518-02b8-3322-92f3-b1965ee5a013 | -5.76513 | -45.09475 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 37d97ac5-808d-36a7-916e-20aea2f9caf1 | -6.42918 | -56.10596 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc1a445d-0393-3fc2-bd45-85fecef606d1 | -6.24303 | -51.69037 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b15b316c-fd82-3b9b-a839-11348379aa23 | -4.35557 | -54.77425 | 2026-09-12 05:10:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7227dd6f-03c9-3ed4-a20e-5258aed08894 | -11.3741 | -46.83579 | 2026-09-12 05:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93ed952d-e0d6-394e-8bca-82e157d22588 | -8.07283 | -54.85086 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ace61aae-e889-300f-b00a-c1cca6b62b46 | -2.67301 | -57.50859 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02fa8f79-2409-34da-bcbe-105f764ec1b2 | -9.71029 | -54.35131 | 2026-09-12 05:10:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7af1295b-5370-32bb-aeaf-293fdd10de19 | -8.50773 | -50.15019 | 2026-09-12 05:10:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9addf216-d663-33ea-831d-1666f9d03df8 | -6.38152 | -58.28786 | 2026-09-12 05:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 353f731a-5eca-315f-9383-b834f191bbc2 | -8.31885 | -54.76528 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c050a3e-4dcf-3121-a384-836bbac79e5d | -7.96561 | -43.99878 | 2026-09-12 05:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56c51702-1441-3e79-af2e-cdb4b60ccbad | -6.12116 | -55.63593 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a452813c-a853-38c1-8530-4671307ae704 | -6.92052 | -55.63821 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1f18315-ec3d-3efc-aa1b-24691660e34c | -6.19886 | -55.26284 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12af7cae-88a9-3cfc-b6d6-57feede97476 | -6.85568 | -47.43817 | 2026-09-12 05:10:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffd062cb-5c0d-3207-9e38-5682c0abc602 | -10.56668 | -51.35804 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70850bcf-b6a3-3501-bb0c-a2136d2d71d8 | -8.14549 | -54.81587 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 665d6156-59d1-3851-8346-1b2ffaf4776b | -2.72985 | -57.64352 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1b165aab-87bc-3d5b-bec4-8ab710e77158 | -5.96756 | -57.77302 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README42.md)
