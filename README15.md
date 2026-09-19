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
| ae2f1856-c4c4-3c33-a7c3-57f7b64776d0 | -11.0082 | -54.124298 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8dd50c0-8fcc-3bc2-8913-3f85b34a93a2 | -14.8646 | -47.144199 | 2026-09-19 00:41:00 | METOP-C | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1e0688ad-a73c-32a7-93de-063c1d847022 | -15.079 | -49.609901 | 2026-09-19 00:41:00 | METOP-C | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bddc840d-85d6-3caa-8395-04b55fd65820 | -21.0259 | -47.265499 | 2026-09-19 00:41:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6ab74c3e-1961-3755-b3ef-3195ee0081a5 | -1.4204 | -49.426201 | 2026-09-19 00:41:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5cac8c2-d6b8-3303-826e-199d3421b65c | -13.6297 | -46.929901 | 2026-09-19 00:41:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d0f74a9c-df1f-3fe6-8ae0-caa12e433c68 | -9.754 | -45.071301 | 2026-09-19 00:41:00 | METOP-C | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7050b7d1-e84e-3a34-ad1a-ff78d012cae2 | -11.0702 | -50.678699 | 2026-09-19 00:41:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 38b35fbb-e16d-323b-a8a4-506aa9a2fe69 | -7.2126 | -49.630901 | 2026-09-19 00:41:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8719d9a-638b-39b8-9004-24d60cd7af89 | -11.3708 | -44.142399 | 2026-09-19 00:41:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 53940a47-c8e0-315e-84d5-a1509077eba6 | -3.7497 | -44.3862 | 2026-09-19 00:41:00 | METOP-C | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bdb99005-5c0a-3125-ac89-69d7bed194b7 | -9.0121 | -44.907101 | 2026-09-19 00:41:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 741e8680-0d01-30d2-8d98-62a269664efd | -5.8651 | -52.0532 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34e40d5c-3282-3e84-a9a1-03e852587270 | -12.9983 | -46.966999 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| efa0b735-7c5f-3179-89a5-3859cb664b3b | -1.1896 | -54.215302 | 2026-09-19 00:41:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e051afbe-147e-3b30-8ba8-730eb7488646 | -12.6012 | -50.922501 | 2026-09-19 00:41:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d3aea6ac-dbf3-353c-9162-3b127f4438ca | -11.1285 | -45.287601 | 2026-09-19 00:41:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| df70d650-2e64-3ebf-9cdd-7621162a32b7 | -5.4901 | -45.813499 | 2026-09-19 00:41:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2dcc7936-7b81-3d23-9c4a-a4035ac910f1 | -11.0678 | -48.269402 | 2026-09-19 00:41:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf576133-a26f-34bb-94e1-2fdac7426101 | -7.1835 | -50.821999 | 2026-09-19 00:41:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 676b67cc-e80f-3ce7-9fcd-6cadb1df665c | -10.9349 | -47.912899 | 2026-09-19 00:41:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aeac4dd3-a234-3500-b2df-dc9b4f9e34bf | -11.9449 | -50.1227 | 2026-09-19 00:41:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89f6bd6d-4491-3eef-a9b7-9a1ba645cdff | -1.409 | -49.421501 | 2026-09-19 00:41:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6232fc49-d9bd-3b07-aea0-7dda71313e2d | -14.1732 | -48.752899 | 2026-09-19 00:41:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| de5690f1-9676-3e15-a535-0689f3b58b9d | -7.6993 | -46.119701 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33cfd486-828f-381e-8c6f-7ddfa3a0ecde | -11.3238 | -47.359299 | 2026-09-19 00:41:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89f02a89-3302-3053-9691-1ca5c3801c43 | -13.6101 | -46.934601 | 2026-09-19 00:41:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b37352a4-beff-3083-8c4b-9fe219d81d42 | -5.468 | -48.993401 | 2026-09-19 00:41:00 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 208c8846-6c92-31c0-b5b9-f82373869915 | -4.4193 | -55.510601 | 2026-09-19 00:41:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac056970-e88b-36e0-974f-be2a466554db | -10.9794 | -49.755199 | 2026-09-19 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd987036-0c6a-348f-8ba7-03e6841c6196 | -11.2988 | -51.7314 | 2026-09-19 00:41:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3de642b-393e-34f5-bf29-ff4deb1c6351 | -11.9139 | -50.1217 | 2026-09-19 00:41:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 105ea04c-1900-364c-a104-dc8ef95ab7eb | -1.31 | -55.820599 | 2026-09-19 00:41:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52251cd0-332c-35e1-906e-b63d747887fb | -15.6805 | -52.761002 | 2026-09-19 00:41:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 672fbc2b-4980-34f8-9f19-2ac8cf6604db | -5.8125 | -49.865799 | 2026-09-19 00:41:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0871f8ab-045b-3136-8e14-3b3e94701a58 | -13.0016 | -46.936401 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 369ac62f-51c7-3533-9208-23ec74536754 | -6.2046 | -45.344601 | 2026-09-19 00:41:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e7bfedd-2a28-3c02-9e5f-e426b46fe6da | -11.3717 | -44.1031 | 2026-09-19 00:41:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 13becc71-c6c6-3f91-941d-a8de68851eca | -4.6028 | -42.960701 | 2026-09-19 00:41:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a93eb2bf-20fe-306f-8688-a6c99b2e5406 | -12.393 | -48.478802 | 2026-09-19 00:41:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 60abeca2-97a5-360d-a6d7-1c7d52a3940c | -10.871 | -54.053501 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1572f134-6bfd-361c-b7ca-13a17a982635 | -10.3989 | -48.320702 | 2026-09-19 00:41:00 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad38c024-b907-3c1b-bda6-0b910df69047 | -1.7042 | -54.891998 | 2026-09-19 00:41:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eff73d44-ed51-360c-9000-e03a711c817c | -3.2409 | -46.9543 | 2026-09-19 00:41:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d313d45-8780-38e1-ae93-706e373dc24e | -21.0243 | -47.257999 | 2026-09-19 00:41:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 88c48a94-5a57-3cb6-8142-eeba3fb9a989 | -9.026 | -48.721298 | 2026-09-19 00:41:00 | METOP-C | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 560b5ba3-cee7-3a0b-a133-7880f35bd917 | -13.6134 | -48.317501 | 2026-09-19 00:41:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b501edc2-3639-3ac8-a4db-965cad2a7d1e | -13.0065 | -46.9576 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac4caa2d-3da9-376b-bfe6-a7f6bbd09b59 | -12.9788 | -46.9716 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d816856f-bc4d-3a53-bf87-67bf961d0f75 | -10.8548 | -56.197201 | 2026-09-19 00:41:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2935621a-7969-3471-9141-325357984da8 | -8.4217 | -54.729698 | 2026-09-19 00:41:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db05e88f-7b9a-38de-8335-b6145754ae38 | -10.7973 | -50.8866 | 2026-09-19 00:41:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 828c427a-b282-36ff-a6bd-b4852d52b3ca | -11.8775 | -47.614101 | 2026-09-19 00:41:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 26d16a70-e3fb-348e-b0a1-ddfe5952304c | -13.6232 | -48.3153 | 2026-09-19 00:41:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b6bf43d3-e48b-3bd8-8ba7-7356e08bfeb7 | -9.8981 | -46.5546 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae7a87da-6827-3d3b-bcaf-d1fec3850483 | -16.050501 | -49.982498 | 2026-09-19 00:41:00 | METOP-C | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 435475ee-f9bf-32f8-8c1e-0fca4eb20dc0 | -13.6313 | -46.937 | 2026-09-19 00:41:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e403c573-ce63-3c76-8ff4-e9b9d7ce46b9 | -8.4727 | -44.510502 | 2026-09-19 00:41:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 11173c5e-5c1a-36be-aaf1-719bbccceb75 | -5.9097 | -46.323299 | 2026-09-19 00:41:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6494067-628f-3272-acc7-f8b4c6cc6f1a | -5.991 | -51.7897 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19cfed9b-936c-3a95-9fe2-6b057b540144 | -1.5853 | -55.5424 | 2026-09-19 00:41:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56f1a147-aa09-326f-a801-8673af472fd1 | -11.5002 | -47.723598 | 2026-09-19 00:41:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 149da2db-bcaf-310c-88c1-d38edb9866e4 | -7.6077 | -45.427601 | 2026-09-19 00:41:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 967312dc-8ca8-3141-a470-e26f8230b88f | -6.6529 | -51.483898 | 2026-09-19 00:41:00 | METOP-C | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2994c88e-13fa-3c93-84ef-2c8046c7eefe | -2.7377 | -49.456902 | 2026-09-19 00:41:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ccd8a9c-1fc3-38b9-8e85-a43fc5d564c7 | -13.8748 | -48.012402 | 2026-09-19 00:41:00 | METOP-C | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0f7d3403-5240-38cc-b2a5-6086528b1580 | -7.6368 | -46.117298 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bbd541c3-48f5-32e7-8706-2d59b7082849 | -14.9618 | -47.5298 | 2026-09-19 00:41:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3332b110-defb-34ec-831e-1de12bdf2795 | -11.332 | -47.349998 | 2026-09-19 00:41:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89e67d14-d4ab-3f06-91dd-16bd61a5aa9a | -9.0457 | -48.7169 | 2026-09-19 00:41:00 | METOP-C | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 9b1dca75-a0b7-36c6-bb7c-2f54ab101581 | -9.7638 | -45.068901 | 2026-09-19 00:41:00 | METOP-C | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c82e0278-ba7a-3ad3-bb18-28b6d6b0a991 | -6.0034 | -49.168098 | 2026-09-19 00:41:00 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d58f2294-8aa2-3642-a19c-dafa7dd4b5ec | -3.4282 | -50.666302 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ce1ffe3-05de-3f36-b7b2-900595794f2f | -7.0301 | -44.651699 | 2026-09-19 00:41:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1eed5daf-c21b-3698-8c66-a8f379b0ae4a | -3.7237 | -54.6465 | 2026-09-19 00:41:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8daa0308-6773-3508-9a2c-b94c2330f9f9 | -10.8514 | -56.180801 | 2026-09-19 00:41:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ecd4e990-dc21-3e92-991a-c3d1f8591e7b | -18.869699 | -49.507401 | 2026-09-19 00:41:00 | METOP-C | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5812b63c-bc4a-30f4-8c50-c1d8a074a2b7 | -5.2192 | -49.301701 | 2026-09-19 00:41:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22a99a14-0ea1-35e4-9534-ce57f5e39f5c | -10.2735 | -50.004601 | 2026-09-19 00:41:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f3036c0-9dfc-37fa-a8df-70f402114a47 | -13.6443 | -46.948799 | 2026-09-19 00:41:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d5d2e4cc-0412-3a57-8c34-94b6ba124774 | -6.6322 | -47.780201 | 2026-09-19 00:41:00 | METOP-C | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3cac3578-6ab3-3e00-9e71-c5cd938175bf | -13.6378 | -46.920502 | 2026-09-19 00:41:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9f543de8-c47a-3ce4-9869-bb553c579fa1 | -11.0741 | -48.297199 | 2026-09-19 00:41:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 381b624e-f5b3-38c9-a07b-fdd6df1c35c5 | -12.1302 | -47.006901 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f64c34d2-95ae-35f7-9f11-abe82af4d540 | -1.4188 | -49.4193 | 2026-09-19 00:41:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b301418-64ce-3c4f-96ed-2c40a10886f1 | -5.5104 | -43.778999 | 2026-09-19 00:41:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 478ee00b-1b08-3bfa-b514-6d20e5429011 | -13.6394 | -46.927601 | 2026-09-19 00:41:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 29f43859-56e0-30d3-a6dd-fe2e7dec54d3 | -4.5671 | -42.983501 | 2026-09-19 00:41:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d6094565-5ac1-3c75-a476-30c66c21ef39 | -3.0342 | -48.4179 | 2026-09-19 00:41:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2d62222-39da-3f37-a6e2-cdd239b979f0 | -6.0008 | -51.787601 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2d9bfe8-26b7-3f89-ba96-75c5a21df681 | -12.5747 | -49.1082 | 2026-09-19 00:41:00 | METOP-C | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 43aa4f8d-da31-3aa5-b5ad-f5a14f6d8ba4 | -1.6293 | -55.149399 | 2026-09-19 00:41:00 | METOP-C | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dd847ee-5415-3d7c-872e-1694f224337e | -14.1414 | -45.1763 | 2026-09-19 00:41:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fc91c7aa-9bbb-3c41-878e-8ff8d4e31620 | -11.9774 | -52.464699 | 2026-09-19 00:41:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e13ea07a-c89c-316c-83b3-3b0415b07f85 | -3.3681 | -50.4491 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 362af59e-98e0-35dc-937a-39fe1fae65c3 | -7.7586 | -46.722698 | 2026-09-19 00:41:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40f8b42f-75fe-3c3e-99fe-2130a32c3dfd | -11.3333 | -43.350899 | 2026-09-19 00:41:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4539ddb0-d7e1-348d-b459-ea3a02871809 | -15.6661 | -52.739899 | 2026-09-19 00:41:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9b4d5da9-b5ba-334b-80e3-94310a5f7da0 | -12.603 | -50.930801 | 2026-09-19 00:41:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 60a6cd2b-0fc7-38fb-b095-973d616d27a5 | -19.5602 | -47.665901 | 2026-09-19 00:41:00 | METOP-C | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README16.md)
