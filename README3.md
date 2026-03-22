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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c108a67-49f4-38d6-a7be-f6dec75b696d | 2.6518 | -61.3015 | 2026-03-22 04:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 237.7 |
| 993e1018-8049-3871-8f48-ac9ca4c4bc52 | 0.9761 | -59.3811 | 2026-03-22 04:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 9be06101-0838-308c-aa1a-d914b0880bdd | 0.9943 | -59.381 | 2026-03-22 04:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 52.1 |
| c604467f-a100-30d1-a878-49ef2f76176c | 2.6519 | -61.2826 | 2026-03-22 04:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 165.7 |
| 2b03eaca-0834-3062-9365-5b82700627d8 | 2.6336 | -61.3017 | 2026-03-22 04:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 6db24292-661f-3bea-beec-04bf077cadc0 | 2.6336 | -61.2828 | 2026-03-22 04:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 51.6 |
| f0e2dac2-e600-33c3-9e8b-3e09ed298874 | -19.47016 | -44.76546 | 2026-03-22 04:00:00 | NOAA-21 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4a5e9d2-6f5a-3626-a736-d13fd288e755 | -20.9001 | -48.80961 | 2026-03-22 04:00:00 | NOAA-21 | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5d0ed51e-daf9-3baa-9422-738e7ae275ab | -21.8556 | -47.17992 | 2026-03-22 04:00:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a2993d0-2d6a-3f01-902b-84651aba4aba | -22.16263 | -51.36665 | 2026-03-22 04:00:00 | NOAA-21 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0d94e22a-c90b-3914-88d8-43cf84b4e97d | -21.46939 | -48.54242 | 2026-03-22 04:00:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0008cce4-d13c-3a62-bdae-d08f6167de8e | -22.97236 | -43.62209 | 2026-03-22 04:00:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bab53e4d-169f-35c2-bc1c-e94fa7a8bf19 | -23.59422 | -46.43158 | 2026-03-22 04:00:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d9352eb4-b652-3e8f-8d7f-ffdf728e9d1d | -20.19752 | -46.50327 | 2026-03-22 04:00:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4fcc90f5-25c7-3853-a70e-321dc55da6e1 | 2.6518 | -61.3203 | 2026-03-22 04:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ea3e140b-83dd-3ca4-8f0f-b63d85ac59ee | 2.6336 | -61.3017 | 2026-03-22 04:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| e6fffa59-d127-336a-b66f-4d04d8ebdd46 | 2.6519 | -61.2826 | 2026-03-22 04:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 1224e670-ab3d-3d4d-a51c-5798bbfe1ba2 | 0.9761 | -59.3811 | 2026-03-22 04:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 49.1 |
| db548510-a49c-3076-a151-0244088bcbcf | 2.6518 | -61.3015 | 2026-03-22 04:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 226.1 |
| e784a618-346d-37c8-a4bb-ede50e361faa | 0.9943 | -59.381 | 2026-03-22 04:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 007f9492-d1fb-39b6-bb30-eaedaa29391a | 2.6519 | -61.2826 | 2026-03-22 04:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 2e565d78-7cee-3d46-adcd-66d6aadace09 | 2.6701 | -61.3012 | 2026-03-22 04:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 127ca225-14fd-3a62-b3f8-b7183a0c59bc | 2.6518 | -61.3015 | 2026-03-22 04:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 189.8 |
| b428dc80-fc7c-31df-b5df-5f2712e60611 | 0.9943 | -59.381 | 2026-03-22 04:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 05888065-3a59-312c-a066-c0479ea5cc21 | 2.6336 | -61.3017 | 2026-03-22 04:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 49.2 |
| d8c2eee8-be72-34bb-ba2c-28c10e56fab2 | -11.32962 | -55.28815 | 2026-03-22 04:27:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec64f121-b36f-3c73-8895-1b732afd8b67 | -12.50199 | -43.68161 | 2026-03-22 04:27:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18e13b26-8526-35da-b857-3f33a52ebc45 | -11.33435 | -55.29268 | 2026-03-22 04:27:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf4e2aad-4227-3376-914e-137cdb70b590 | -11.78508 | -41.19596 | 2026-03-22 04:27:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3dfd45af-c7e9-3ded-b16d-0e2eb664f1cb | -12.50606 | -43.67823 | 2026-03-22 04:27:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1af219d6-10df-3b04-81aa-ebdd8eadea0e | -12.49674 | -43.64463 | 2026-03-22 04:27:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6df75af5-a8ae-3d13-8992-d4ca97138486 | -12.49616 | -43.64856 | 2026-03-22 04:27:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75784688-ba65-34e5-97b8-d39c32a804a6 | -12.49266 | -43.64802 | 2026-03-22 04:27:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 534bf1fc-4428-38a4-bb0f-aae666ff92d8 | -11.32895 | -55.29164 | 2026-03-22 04:27:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30062e0c-ae9d-311f-a508-dc13a3960fcb | -11.33501 | -55.28925 | 2026-03-22 04:27:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d690e2e-3c83-32ed-8f70-1eea5f0f4fba | -12.50315 | -43.64963 | 2026-03-22 04:27:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfa7ab1b-b5ab-39cb-a717-51b90142a48f | -11.3337 | -55.29613 | 2026-03-22 04:27:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9ad1e0f-59f5-3a02-908f-516e7581497d | -12.50548 | -43.68216 | 2026-03-22 04:27:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 142e06b2-f495-32b8-864e-9a26e0056785 | -11.32419 | -55.28723 | 2026-03-22 04:27:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d92d8b5-8ae2-35d4-a122-3c0c1997a28f | -11.32829 | -55.29514 | 2026-03-22 04:27:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0979204-f783-3325-85a6-95d555ccc962 | -20.19499 | -46.50134 | 2026-03-22 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6ef5a00-7c44-35d0-acb2-b18754371e55 | -21.85409 | -47.17866 | 2026-03-22 04:29:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9e227b04-50b4-30d4-ad4c-f79cc38e0707 | -21.85351 | -47.18245 | 2026-03-22 04:29:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| b271b827-8dbb-3ee0-bf96-d812ee91d0ed | -20.89699 | -48.81096 | 2026-03-22 04:29:00 | NPP-375D | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0216b981-4d95-3c7d-99c9-deb9ab098b22 | -21.46782 | -48.54214 | 2026-03-22 04:29:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ba294d1f-5564-37e1-bb09-bf9ccbd444c4 | -20.19836 | -46.50195 | 2026-03-22 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39f08a7e-032b-3554-90b4-ec24ea7626a4 | -19.99157 | -54.73917 | 2026-03-22 04:29:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 830c5728-2139-3f05-9890-386afc041559 | 2.6336 | -61.2828 | 2026-03-22 04:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 11022c11-cbe7-39e2-af9d-046ed345ef8b | 2.6518 | -61.3015 | 2026-03-22 04:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 9e5f75a8-2c57-38dc-924d-5485e5e9f5ef | 2.6519 | -61.2826 | 2026-03-22 04:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 182.9 |
| 66d5ba0a-ca98-396d-8f3c-7a38b20a4e31 | -22.16376 | -51.36831 | 2026-03-22 04:32:00 | NPP-375D | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 6626b48c-035e-3ba0-addf-177b5d9b4d72 | -21.66574 | -56.32401 | 2026-03-22 04:32:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c10caac-00d5-3154-920a-1156922d8271 | -23.59291 | -46.43296 | 2026-03-22 04:32:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| eed96d3f-996c-3a9c-ad11-c495930ca1a2 | -25.54094 | -52.92354 | 2026-03-22 04:32:00 | NPP-375D | QUEDAS DO IGUAÇU | PARANÁ | Brasil | 4120903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 70ccd15c-7d71-3ed7-959e-b388845a4da7 | -31.01305 | -50.80344 | 2026-03-22 04:34:00 | NPP-375D | MOSTARDAS | RIO GRANDE DO SUL | Brasil | 4312500 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| e6ce7fe5-3abe-30a7-a1ce-043eb14f399e | 1.0832 | -59.72998 | 2026-03-22 04:46:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8be4c90-17c0-3bea-9db6-7300c7f01ba6 | 2.65137 | -61.28828 | 2026-03-22 04:46:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 25.1 |
| ecbbcf5d-bd04-343b-8eeb-ba72b3c9b556 | 2.65218 | -61.29377 | 2026-03-22 04:46:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 27.5 |
| a71ac156-d6f6-38e3-9858-36be71af8b07 | 2.64485 | -61.28915 | 2026-03-22 04:46:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 25.1 |
| d1a06b84-cf49-3796-886d-add771099581 | 0.86543 | -60.24955 | 2026-03-22 04:46:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3931f59-8df2-3560-814e-a393416e0884 | 1.08381 | -59.73405 | 2026-03-22 04:46:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b824196-fcec-31b7-862f-0a98719f5b8a | 0.98688 | -59.37986 | 2026-03-22 04:46:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 78dffbcc-156a-3390-9383-41845302081a | 2.6579 | -61.28751 | 2026-03-22 04:46:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b8cb84ef-ac45-388e-84ff-cea00a391eb7 | 2.65457 | -61.30989 | 2026-03-22 04:46:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 4a910033-f3fc-3db4-8b39-333c3253b604 | 1.47777 | -50.90837 | 2026-03-22 04:46:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f787f80d-9623-3acc-942b-9304b0e73e45 | 0.84986 | -59.99108 | 2026-03-22 04:46:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b518ca6-607d-380d-8e1b-961974f634d4 | 2.65376 | -61.30443 | 2026-03-22 04:46:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f654280f-3364-3fd5-ac8e-aacb91bb780c | 2.65872 | -61.29299 | 2026-03-22 04:46:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 79d85384-84b0-3fae-9cf1-78fbae686c6e | 3.23546 | -61.20039 | 2026-03-22 04:46:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1d5c20b3-eda2-326c-8b58-fea664a24b49 | 3.23535 | -61.19574 | 2026-03-22 04:46:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67484268-70ac-3a89-b355-6e53121d3384 | 1.55538 | -60.25072 | 2026-03-22 04:46:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 896e98f1-e9ad-312f-bb96-8c0fc622d948 | 2.59371 | -60.60002 | 2026-03-22 04:46:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e9f9a4f-d51d-3ed5-8517-f362594c0b65 | -3.18486 | -52.88646 | 2026-03-22 04:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 003548ef-0371-339e-8a0c-ee24b6aa7410 | 0.98747 | -59.38363 | 2026-03-22 04:46:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 88793338-4fcc-3175-9d7f-abab1ff67ec0 | 2.64644 | -61.29993 | 2026-03-22 04:46:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 27.5 |
| d5930dbf-34bc-3eca-acb9-dd21a1c3e170 | 1.08784 | -60.34808 | 2026-03-22 04:46:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 261c8d0c-abc5-3d38-911c-942a4ad02286 | 0.98126 | -59.38074 | 2026-03-22 04:46:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| db823e21-f5d7-3425-9061-fba00927f18c | 0.5752 | -59.90807 | 2026-03-22 04:46:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77535836-34fc-3c11-ab54-48a0de817080 | 2.64724 | -61.30532 | 2026-03-22 04:46:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b181562a-9ae8-3135-9024-b32a8afa4fb6 | 0.9925 | -59.37896 | 2026-03-22 04:46:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 280abf98-a594-3356-8276-a7f4d71edeb7 | 1.54937 | -60.25163 | 2026-03-22 04:46:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ae70547-e1eb-3988-b318-57dc3ac68f0f | 0.98805 | -59.3874 | 2026-03-22 04:46:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 16.3 |
| b88f77ea-b7a7-33ae-8b36-705abb3688b1 | 0.99367 | -59.38647 | 2026-03-22 04:46:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 33052b1c-ac7b-3f24-9a04-04e58cd0d02f | 0.99192 | -59.37523 | 2026-03-22 04:46:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 593ed4ca-08cf-32c7-96b7-5fca24633154 | 0.8595 | -60.25053 | 2026-03-22 04:46:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f7b5031-d025-33b6-a11d-45df12056528 | -1.49918 | -53.67946 | 2026-03-22 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb0f0a53-6fab-39d7-ac1c-5beb5a9414bd | 2.64564 | -61.29453 | 2026-03-22 04:46:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 27.5 |
| e9fabc94-472c-3a01-812e-322298cefce4 | 0.99426 | -59.39026 | 2026-03-22 04:46:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 71cf20ca-9fef-3ffd-b649-df2ee631ea98 | 3.23618 | -61.20127 | 2026-03-22 04:46:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 930d2824-c468-3434-84bd-c4b970e8bbf9 | 0.99308 | -59.3827 | 2026-03-22 04:46:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5d171c94-1849-326c-bd19-54cc012a7d47 | -0.08762 | -51.27861 | 2026-03-22 04:46:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eef3863e-2c20-3849-9dcd-7d0db2269e9b | 1.64467 | -60.29838 | 2026-03-22 04:46:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab1519c5-ad93-32f5-ac86-9702a5d3122c | 1.25909 | -60.44775 | 2026-03-22 04:46:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6c9ed4c-07a7-3959-82b7-e70e520316f5 | 1.04472 | -60.36327 | 2026-03-22 04:46:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 225d4d5f-e43d-316f-bd1c-b0f2dab68a94 | 1.12393 | -60.18516 | 2026-03-22 04:46:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e1bcba5-d904-3ac5-9c74-f1aa970d3c54 | 1.04402 | -60.3588 | 2026-03-22 04:46:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0bbb5f3-275f-347f-8c7d-bda667bd5381 | 0.57567 | -59.90835 | 2026-03-22 04:46:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 909edea7-39fc-39b2-bc10-cd17128fbcdd | 2.12354 | -61.2227 | 2026-03-22 04:46:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9ac0e363-4667-36eb-a117-ffbe32d3d265 | 2.65297 | -61.2991 | 2026-03-22 04:46:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 183b8974-e3f6-36a6-bead-5a5815151246 | 0.9863 | -59.37612 | 2026-03-22 04:46:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |


[Clique aqui para ver as próximas entradas](README4.md)
