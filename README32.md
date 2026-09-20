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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0385a039-4ec5-33a7-846f-07381ce9c0b5 | -7.30891 | -55.61393 | 2026-09-20 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e1b7d0a-a14e-3058-bb25-c2aeeec7d119 | -9.2557 | -45.927 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49095920-5e16-3669-b4a2-6ed330ec53b5 | -10.93336 | -48.31464 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 821aeb5d-46bd-3b2c-9786-64e2fe7b5ffb | -9.23724 | -45.91704 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d8dcee1d-d6de-320c-bb71-48950f90e4e8 | -11.45755 | -45.70446 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eece0033-696f-3fe4-b3cd-bdbf3ad1a328 | -9.80862 | -48.33085 | 2026-09-20 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89c5f098-b7d9-33b9-8cb9-6dde2de163e5 | -5.64426 | -43.37135 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60525c5b-40f0-3fd7-963e-b69b6767c665 | -7.95648 | -45.28552 | 2026-09-20 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93985bec-5abf-3cfc-847e-34b080dc7d6e | -8.3572 | -47.25208 | 2026-09-20 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9e15158-4f46-3863-b726-b41fcdebbda0 | -9.01723 | -44.92875 | 2026-09-20 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| defd646c-3787-3486-8d5f-9eba0b85a334 | -11.06094 | -49.7411 | 2026-09-20 04:19:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 540042f0-a083-3421-80cb-2399b181a081 | -10.31544 | -50.21958 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9c7a1e1c-9123-33cf-9b38-5d3908451cfc | -8.37959 | -45.63863 | 2026-09-20 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6848909a-6486-3cf8-b0f5-eac0ece96bf2 | -8.60893 | -47.30709 | 2026-09-20 04:19:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d27a178-8b14-304c-8347-1f5bad3410a4 | -10.30768 | -50.2627 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f48564d4-63d3-3eae-b795-24b6dc6aa60c | -10.30866 | -50.22942 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25bc8077-b2ef-34a2-8afa-d5029ee9e57d | -7.59354 | -46.73027 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce80ca6b-1b8d-35b7-8616-f27bf89371a7 | -5.7649 | -47.2853 | 2026-09-20 04:19:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a08ded56-dca2-3a41-8083-54a7b0acf543 | -2.9786 | -54.76981 | 2026-09-20 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88c3ee37-a2b1-3e50-8c49-8341b2c9b820 | -8.85258 | -45.93155 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5aa98240-bde9-3adc-a5ad-691c92d4a3ae | -8.49506 | -47.43713 | 2026-09-20 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6f61b82-3f52-3f5f-b0c7-2d140a8ce384 | -4.25535 | -48.54193 | 2026-09-20 04:19:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb552dc0-3723-3c53-a2c0-ef6c1ad676cd | -6.17415 | -47.71803 | 2026-09-20 04:19:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a294209a-4fa4-3b19-bcf1-6cdd9b521686 | -5.61919 | -40.85359 | 2026-09-20 04:19:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f1a862c1-5201-3014-86f4-7086c71b8820 | -3.89402 | -49.09036 | 2026-09-20 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53b13891-6d91-37fc-9b5e-3e04768c351b | -6.54526 | -44.93051 | 2026-09-20 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1208f871-ce57-3141-9922-73cda9a41616 | -5.22405 | -42.72699 | 2026-09-20 04:19:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 38405e69-7549-3bcf-808e-7cb302157699 | -9.0477 | -48.71406 | 2026-09-20 04:19:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8b32990f-abd7-347f-a7e2-125c5fbb7224 | -10.46026 | -45.08921 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83665a31-5339-3d13-b077-a463c0c5030e | -6.29966 | -41.76547 | 2026-09-20 04:19:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 421c70e4-c660-32cc-9502-957a3907f17b | -7.43197 | -44.73565 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2371f8bc-130f-356c-8950-8a6948aafff2 | -9.7008 | -54.82793 | 2026-09-20 04:19:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df339bff-6b92-383b-9599-adc7d584eadd | -7.76828 | -44.05215 | 2026-09-20 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0f4e2ce0-d958-318f-b762-455e083aae08 | -7.6245 | -45.46437 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 93defb96-4a31-3945-bfee-b798774e6320 | -5.76739 | -47.2845 | 2026-09-20 04:19:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24239f3b-df52-3e8b-8272-5783c94ff4dc | -6.20844 | -45.35439 | 2026-09-20 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9de3862b-c45c-35ba-a065-875b4638b7f1 | -9.17527 | -51.51337 | 2026-09-20 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4139c069-f55f-3a99-b8ad-254fd1164503 | -11.47232 | -47.78663 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17de816f-6fd6-3291-a6ce-9cb8a0331ed2 | -5.65973 | -43.20898 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4b484cc8-7ad4-3c65-894e-7d0934b6655a | -8.32699 | -50.9458 | 2026-09-20 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe112a1e-734a-35fc-a83f-cd69a7e61fa0 | -6.5156 | -46.78013 | 2026-09-20 04:19:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 52014610-f56b-3efb-af08-332889f77f79 | -11.2385 | -48.37661 | 2026-09-20 04:19:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a1fdbb5d-e8b2-3330-920a-ec2274b8a1bc | -8.16292 | -54.82693 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 48dbe3a1-0983-39e6-9c62-e310c6e14bcd | -5.85036 | -53.50515 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2d83b45-392c-39e5-a90a-e6c0426909b1 | -7.35066 | -44.61818 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33b22d88-dbd0-34dd-95a5-d5e604002884 | -5.87424 | -51.55977 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 537d4fef-2f06-3a31-baf1-c2dbe3f9c710 | -7.43587 | -44.6898 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f1348a8-3916-3ce1-8c2c-14d077aeb1dc | -8.43619 | -46.86392 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc9a47d9-9604-3a0f-b8c5-6e094e8c1e72 | -7.55435 | -45.44078 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c5d5ccdf-3365-3324-be02-4a8574c88d1f | -7.16201 | -47.4694 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 366bc3a9-fc37-374b-a6fa-af79778d9aac | -5.84627 | -53.56681 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f97d3f05-3691-3f88-ae87-d0b3bdcafbd9 | -7.55282 | -45.42694 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e597193f-c4a4-3833-a7fc-9862bfab657c | -9.61666 | -45.87293 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f207121-f8fd-34e1-a9b0-029ae90b9902 | -6.41132 | -42.8156 | 2026-09-20 04:19:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b3d261ad-37e7-3caa-9dc3-e345ea25f57d | -6.91917 | -42.91174 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b7038132-509a-3f4e-9204-48f273b34bec | -4.91166 | -49.04397 | 2026-09-20 04:19:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca050e1c-21ca-342c-a369-93f4dfd2038d | -6.22279 | -44.69061 | 2026-09-20 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0a1d59d1-ea71-3cd0-8b16-8fa326178073 | -9.58986 | -45.36919 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55721547-340a-3e8e-87cd-789cff61b8cc | -9.83428 | -46.43435 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 085e5e9b-f231-352c-8b01-abd994e36185 | -8.18406 | -40.81852 | 2026-09-20 04:19:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bfc40cd6-c011-30e3-9d6f-e69fa8c79baf | -9.92517 | -48.38461 | 2026-09-20 04:19:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a529971-901c-36f8-b4b0-f52e51dd4562 | -5.46682 | -45.61469 | 2026-09-20 04:19:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6d0e29a-62a5-3d95-a12c-0a7a6131ce80 | -8.61266 | -54.59531 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fc06b7c5-6745-3908-bf4a-9a31307d8c3f | -3.00834 | -54.17347 | 2026-09-20 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0cd5a04-28d2-3421-8d2a-5252089688f9 | -10.46422 | -45.08465 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab0e0c94-75d5-37fe-8284-00adeb9b4425 | -10.297 | -50.26624 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 6bbb006c-329e-3c5f-b1e7-92a61cb1af5a | -10.29411 | -50.25451 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a72d4ac-e287-351d-84ed-31286a22936b | -11.14633 | -42.79613 | 2026-09-20 04:19:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b8024990-e07c-3a7a-afce-891f016e32e1 | -10.13372 | -45.5534 | 2026-09-20 04:19:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c90290b1-dcf2-3310-978d-af363ee38c1a | -8.4463 | -43.85767 | 2026-09-20 04:19:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e389a1d2-7060-3ecf-9e66-ace81b0bddad | -5.09847 | -47.50996 | 2026-09-20 04:19:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 83f334c0-bd68-34bc-9a50-73343e3b5086 | -10.276 | -45.43961 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 678fc890-aaea-319a-aa5a-e2d4b0ef7d30 | -5.8678 | -51.57021 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4934f388-4486-3ce7-a877-fb7d21e73c80 | -10.31671 | -50.22645 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 28ee5ca8-d985-3771-b96f-d434d70dc4c9 | -7.36091 | -44.87294 | 2026-09-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2b6fec0-8081-3934-a579-56eecb4fd41f | -3.9534 | -49.04218 | 2026-09-20 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7dbe3d46-c103-3079-aedd-de5f958a1e41 | -10.87733 | -45.14404 | 2026-09-20 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f597238e-c5cc-3e4a-9e49-46f59681b7b0 | -5.85847 | -53.53587 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 63d68728-3632-339c-9794-097502a68ed6 | -6.45314 | -48.44143 | 2026-09-20 04:19:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e91e8827-3808-37e3-babf-bed64f7376f1 | -7.53477 | -45.88106 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 31bc6f87-68c8-3fdc-af9f-84b5b1f547a9 | -5.79288 | -47.36808 | 2026-09-20 04:19:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b464ce8b-c822-3df1-ace1-0458c299e37c | -10.77849 | -46.3199 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45b85c4b-0a62-3134-8363-f51f305ac9ff | -7.01955 | -45.24268 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17db160e-9e77-3b6e-8013-09ae52d14499 | -9.01355 | -44.99484 | 2026-09-20 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f10179d3-d90c-3ff4-8467-cfe9f9a56ac2 | -8.37053 | -47.19794 | 2026-09-20 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a840730b-1526-3608-ac6a-7482c4381323 | -7.62608 | -46.11961 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 716c28ec-aa47-343b-9762-a474ffbff958 | -5.8397 | -53.56242 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 257ac7cf-9586-36c9-86e4-c9ddebef3200 | -7.12181 | -44.82856 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e37cfdcb-9b75-34b0-8d50-6d0d19f387b2 | -8.61427 | -54.60701 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 807f6c24-1564-3da4-b0e6-daef7f911da5 | -9.54585 | -45.40586 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 600a6f14-0fb9-38d2-be2e-a4f25e9f2088 | -11.02598 | -48.3058 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd68f2ee-d975-3215-8537-ff2289060ead | -11.4702 | -45.33381 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86134a76-a3c6-3688-a679-25fb4398bc65 | -11.074 | -49.49509 | 2026-09-20 04:19:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d630047-3368-3362-b779-2ea7ad9261ea | -8.47784 | -45.09291 | 2026-09-20 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11ba8cf9-5d7b-3a57-bf73-8b52177c193e | -6.66359 | -50.89476 | 2026-09-20 04:19:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b1a7511b-c141-3355-87d6-869c4ad4480c | -8.17203 | -54.77899 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0d64c7cf-ab67-3d13-b86d-c3b0b267854b | -10.4765 | -51.26294 | 2026-09-20 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9037e663-ff7e-3cd4-9a26-556529923fcd | -9.79067 | -48.32452 | 2026-09-20 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ae1a77a-0bdf-3026-bf35-2103804a65c3 | -9.54664 | -45.40469 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31bc1612-ac82-375b-a407-bb5b13b41d99 | -5.84643 | -53.52626 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README33.md)
